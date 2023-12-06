using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Globalization;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace motelfuensavinan
{
    class Ctr571
    {
        //打开串口
        [DllImport(@"CRT_571.dll")]
        public static extern UInt32 CommOpen(string port);
        //按指定的波特率打开串口
        [DllImport(@"CRT_571.dll")]
        public static extern long CommOpenWithBaut(string port, UInt32 Baudrate);
        //关闭串口
        [DllImport(@"CRT_571.dll")]
        public static extern int CommClose(UInt32 ComHandle);

        //int APIENTRY ExecuteCommand(HANDLE ComHandle,BYTE TxAddr,BYTE TxCmCode,BYTE TxPmCode,int TxDataLen,BYTE TxData[],BYTE *RxReplyType,BYTE *RxStCode0,BYTE *RxStCode1,BYTE *RxStCode2,int *RxDataLen,BYTE RxData[]);
        [DllImport(@"CRT_571.dll")]
        public static extern int ExecuteCommand(UInt32 ComHandle, byte TxAddr, byte TxCmCode, byte TxPmCode, UInt16 TxDataLen, byte[] TxData, ref byte RxReplyType, ref byte RxStCode0, ref byte RxStCode1, ref byte RxStCode2, ref UInt16 RxDataLen, byte[] RxData);

        UInt32 Hdle = 0;
        private void Inicializar()
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x30;
                Pm = 0x30;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        //MessageBox.Show("INITIALIZE OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "INITIALIZE");
                        Console.WriteLine("INITIALIZE OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "INITIALIZE");
                    }
                    else
                    {
                        Console.WriteLine("INITIALIZE ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "INITIALIZE");
                    }

                }
                else
                {
                    //MessageBox.Show("Communication Error", "Caution");
                }
            }
            else
            {
                //MessageBox.Show("Comm. port is not Opened", "Caution");
            }
        }
        public UInt32 Arrancar()
        {
            Configuracion config = Configuracion.Instance();
            config.ficheroIni();
            try
            {
                Console.WriteLine(config.COMCtr571);
                Hdle = CommOpen(config.COMCtr571);
                if (Hdle != 0)
                {
                    Console.WriteLine("Comm. Port is Opened");
                    Inicializar();
                }
                else
                {
                    Console.WriteLine("Open Comm. Port Error");

                }
            }
            catch (Exception e)
            {

                Logs logs = new Logs();
                logs.WriteLog("Error no se encuentra la dll ","Error");
            }
       
            return Hdle;
        }
        public void CloseCom()
        {
            if (Hdle != 0)
            {
                int i = CommClose(Hdle);
                Hdle = 0;
                Console.WriteLine ( "Comm. Port is Closed");
            }
        }

        //UInt32 Hdle param

        public void MoveCardToFront()
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x32;
                Pm = 0x30;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        Console.WriteLine("Move Card OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "Move Card");
                    }
                    else
                    {
                        Console.WriteLine("Move Card ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Move Card");
                    }

                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Comm. port is not Opened", "Caution");
            }
        }

        public void MoveCardRF()
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x32;
                Pm = 0x32;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        Console.WriteLine("Move Card OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "Move Card RF");
                    }
                    else
                    {
                        Console.WriteLine("Move Card ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Move Card RF");
                    }

                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Comm. port is not Opened", "Caution");
            }
        }
        public bool CheckCardIC()
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x50;
                Pm = 0x30;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        Console.WriteLine("Move Card OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "check Card IC");
                        return true;
                    }
                    else
                    {
                        Console.WriteLine("Move Card ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Move Card RF");
                        return false;
                    }

                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                    return false;
                }
            }
            else
            {
                Console.WriteLine("Comm. port is not Opened", "Caution");
                return false;
            }
        }
        public void MoveCardIC()
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x32;
                Pm = 0x31;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        Console.WriteLine("Move Card OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "Move Card IC");
                    }
                    else
                    {
                        Console.WriteLine("Move Card ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Move Card IC");
                    }

                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Comm. port is not Opened", "Caution");
            }
        }
        public void MoveCardToWrite(UInt32 Hdle)
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x32;
                Pm = 0x32;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        Console.WriteLine("Move Card OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "Move Card");
                    }
                    else
                    {
                        Console.WriteLine("Move Card ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Move Card");
                    }

                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Comm. port is not Opened", "Caution");
            }
        }
        private void CardStatus()
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x31;
                Pm = 0x30;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        Console.WriteLine("Card Status OK" + "\r\n" + "Status Code : " + (char)St0 + (char)St1 + (char)St2, "Card Status");
                    }
                    else
                    {
                        Console.WriteLine("Card Status ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Card Status");
                    }

                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Comm. port is not Opened", "Caution");
            }
        }
        private void SensorStatus(object sender, EventArgs e)
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x31;
                Pm = 0x31;
                St0 = St1 = St2 = 0;
                TxDataLen = 0;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        Console.WriteLine("Sensor Status OK" + "\r\n"
                               + "Sensor 1 (PSS1):    " + Convert.ToString(RxData[0], 16) + "\r\n"
                               + "Sensor 2 (PSS2):    " + Convert.ToString(RxData[1], 16) + "\r\n"
                               + "Sensor 3 (PSS3):    " + Convert.ToString(RxData[2], 16) + "\r\n"
                               + "Sensor 4 (PSS4):    " + Convert.ToString(RxData[3], 16) + "\r\n"
                               + "Sensor 5 (PSS5):    " + Convert.ToString(RxData[4], 16) + "\r\n"
                               + "Sensor 6 (PSS6):    " + Convert.ToString(RxData[5], 16) + "\r\n"
                               + "Sensor 7 (PSS7):    " + Convert.ToString(RxData[6], 16) + "\r\n"
                               + "Sensor 8 (PSS8):    " + Convert.ToString(RxData[7], 16) + "\r\n"
                               + "Sensor 9 (PSS9):    " + Convert.ToString(RxData[8], 16) + "\r\n"
                               + "Sensor 10 (PSS10):  " + Convert.ToString(RxData[9], 16) + "\r\n"
                               + "Sensor KS1 (KS1):   " + Convert.ToString(RxData[10], 16) + "\r\n"
                               + "Sensor KS2 (KS2):   " + Convert.ToString(RxData[11], 16), "Sensor Status");
                    }
                    else
                    {
                        Console.WriteLine("Sensor Status ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Sensor Status");
                    }

                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Comm. port is not Opened", "Caution");
            }
        }
        private string MiCardActivate(object sender, EventArgs e)
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x60;
                Pm = 0x30;
                St0 = St1 = St2 = 0;
                TxDataLen = 2;
                RxDataLen = 0;

                TxData[0] = 0x41;
                TxData[1] = 0x42;
                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        int n;
                        switch (RxData[0])
                        {
                            case 0x4d:  //mifare one Card
                                {
                                    string CardUID = "";


                                    for (n = 0; n < RxData[3]; n++)
                                    {
                                        CardUID += RxData[n + 4].ToString("X2");

                                    }
                                    // string prueba = "";
                                    //  for (n = 0; n < RxData.Length; n++) { prueba += RxData[n]; }Console.WriteLine(""+prueba);
                                    // prueba = "";
                                    // for (n = 0; n < TxData.Length; n++) { prueba += TxData[n]; }Console.WriteLine("" + prueba);
                                    Console.WriteLine(CardUID);
                                    switch (RxData[2])
                                    {
                                        case 68: //Mifare one UL card
                                            {
                                                Console.WriteLine("Mifare one Card Activate Successed\nMifare one UL card ", "Activate RF Card");
                                                return CardUID;
                                                //break;
                                            }
                                        case 4: //Mifare one S50 card
                                            {
                                                Console.WriteLine("Mifare one Card Activate Successed\nMifare one S50 card ", "Activate RF Card");
                                                return CardUID;
                                                //break;
                                            }
                                        case 2: //Mifare one S70 card
                                            {
                                                Console.WriteLine("Mifare one Card Activate Successed\nMifare one S70 card ", "Activate RF Card");
                                                return CardUID;
                                                //break;
                                            }
                                    }
                                    //MessageBox.Show("Mifare one Card Activate Successed\nCardUID: " + CardUID, "Activate RF Card");
                                    break;
                                }
                            case 0x41:   //type A card
                                {
                                    Console.WriteLine("type A Card Activate Successed ", "Activate RF Card");
                                    return "";
                                    //break;
                                }
                            case 0x42:   //type B card
                                {
                                    Console.WriteLine("type B Card Activate Successed ", "Activate RF Card");
                                    return "";
                                   // break;
                                }
                        }
                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Activate RF Card ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Activate RF Card");
                        return "";
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                        return "";
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                    return "";
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
                return "";
            }
            return "";
        }





        public string MiCardActivate()
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x60;
                Pm = 0x30;
                St0 = St1 = St2 = 0;
                TxDataLen = 2;
                RxDataLen = 0;

                TxData[0] = 0x41;
                TxData[1] = 0x42;
                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        int n;
                        switch (RxData[0])
                        {
                            case 0x4d:  //mifare one Card
                                {
                                    string CardUID = "";


                                    for (n = 0; n < RxData[3]; n++)
                                    {
                                        CardUID += RxData[n + 4].ToString("X2");

                                    }
                                    // string prueba = "";
                                    //  for (n = 0; n < RxData.Length; n++) { prueba += RxData[n]; }Console.WriteLine(""+prueba);
                                    // prueba = "";
                                    // for (n = 0; n < TxData.Length; n++) { prueba += TxData[n]; }Console.WriteLine("" + prueba);
                                    Console.WriteLine(CardUID);

                                    switch (RxData[2])
                                    {
                                        case 68: //Mifare one UL card
                                            {
                                                Console.WriteLine("Mifare one Card Activate Successed\nMifare one UL card ", "Activate RF Card");
                                                return CardUID;
                                                //break;
                                            }
                                        case 4: //Mifare one S50 card
                                            {
                                                Console.WriteLine("Mifare one Card Activate Successed\nMifare one S50 card ", "Activate RF Card");
                                                return CardUID;
                                                //break;
                                            }
                                        case 2: //Mifare one S70 card
                                            {
                                                Console.WriteLine("Mifare one Card Activate Successed\nMifare one S70 card ", "Activate RF Card");
                                                return CardUID;
                                                //break;
                                            }
                                    }
                                    return CardUID;
                                    //MessageBox.Show("Mifare one Card Activate Successed\nCardUID: " + CardUID, "Activate RF Card");
                                    //break;
                                }
                            case 0x41:   //type A card
                                {
                                    Console.WriteLine("type A Card Activate Successed ", "Activate RF Card");
                                    return "";
                                    //break;
                                }
                            case 0x42:   //type B card
                                {
                                    Console.WriteLine("type B Card Activate Successed ", "Activate RF Card");
                                    return "";
                                    //break;
                                }
                        }
                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Activate RF Card ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Activate RF Card");
                        return "";
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                        return "Error";
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                    return "Error";
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
                return "";
            }
            return "";
        }

        private void MiCheckPasswordBtn_Click(object sender, EventArgs e)
        {
            if (Hdle != 0)
            {
                Configuracion config = new Configuracion();
                config.ficheroIni();
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;
                string PasswordStr = "FF FF FF FF FF FF";

                Cm = 0x60;
                Pm = 0x33;
                St0 = St1 = St2 = 0;
                byte sector = 0xff;
                TxData[0] = 0x0;
                TxData[1] = 0x20;
                TxData[2] = 0x0;  //Key A
                TxData[3] = sector;// Sector Number
                TxData[4] = 0x6;   //length of Password ,6 Bytes
                TxData[5] = (byte)Convert.ToInt32(PasswordStr.Substring(0, 2), 16);//0xff;
                TxData[6] = (byte)Convert.ToInt32(PasswordStr.Substring(3, 2), 16);//0xff; 
                TxData[7] = (byte)Convert.ToInt32(PasswordStr.Substring(6, 2), 16);// 0xff; 
                TxData[8] = (byte)Convert.ToInt32(PasswordStr.Substring(9, 2), 16);// 0xff; 
                TxData[9] = (byte)Convert.ToInt32(PasswordStr.Substring(12, 2), 16);//0xff; 
                TxData[10] = (byte)Convert.ToInt32(PasswordStr.Substring(15, 2), 16); //0xff;
                TxDataLen = 11;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        if (RxData[RxDataLen - 2] == 0x90 && RxData[RxDataLen - 1] == 0x00)   //last two Byte(SW1 SW2) is "9000"
                        {
                            Console.WriteLine("Check password Successed", "Check password");
                        }
                        else
                        {
                            Console.WriteLine("Check password Error", "Check password");
                        }

                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Check password ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Check password");
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
            }
        }
        public void MiCheckPassword(string PasswordStr, byte sector)
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;
                //string PasswordStr = "C9 65 4F 67 C9 65";



                Cm = 0x60;
                Pm = 0x33;
                St0 = St1 = St2 = 0;

                TxData[0] = 0x0;
                TxData[1] = 0x20;
                TxData[2] = 0x0;  //Key A
                TxData[3] = sector;// Sector Number
                TxData[4] = 0x6;   //length of Password ,6 Bytes
                TxData[5] = (byte)Convert.ToInt32(PasswordStr.Substring(0, 2), 16);//0xff;
                TxData[6] = (byte)Convert.ToInt32(PasswordStr.Substring(3, 2), 16);//0xff; 
                TxData[7] = (byte)Convert.ToInt32(PasswordStr.Substring(6, 2), 16);// 0xff; 
                TxData[8] = (byte)Convert.ToInt32(PasswordStr.Substring(9, 2), 16);// 0xff; 
                TxData[9] = (byte)Convert.ToInt32(PasswordStr.Substring(12, 2), 16);//0xff; 
                TxData[10] = (byte)Convert.ToInt32(PasswordStr.Substring(15, 2), 16); //0xff;
                TxDataLen = 11;
                RxDataLen = 0;


                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        if (RxData[RxDataLen - 2] == 0x90 && RxData[RxDataLen - 1] == 0x00)   //last two Byte(SW1 SW2) is "9000"
                        {
                            Console.WriteLine("Check password Successed", "Check password");
                        }
                        else
                        {
                            Console.WriteLine("Check password Error", "Check password");
                        }

                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Check password ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Check password");
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
            }
        }

        private void MiReadLockBtn_Click(object sender, EventArgs e)
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x60;
                Pm = 0x33;
                St0 = St1 = St2 = 0;

                TxData[0] = 0x0;
                TxData[1] = 0xB0;  //Read
                TxData[2] = (byte)0x01;// Sector Number  
                TxData[3] = (byte)0x00;//Start Block
                TxData[4] = 0x4;  //Block Numbers
                TxDataLen = 5;
                RxDataLen = 0;
                MiCheckPasswordBtn_Click(sender, e);
                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {


                        if (RxData[RxDataLen - 2] == 0x90 && RxData[RxDataLen - 1] == 0x00)   //last two Byte(SW1 SW2) is "9000"
                        {
                            int n;
                            string StrBuf = "";

                            for (n = 0; n < 16; n++)
                            {
                                StrBuf += RxData[n].ToString("X2") + " ";
                                Console.WriteLine(StrBuf);
                            }

                            Console.WriteLine(StrBuf);
                            Console.WriteLine("Read Block Data Successed", "Read Block Data");
                        }
                        else
                        {
                            int n;
                            string StrBuf = "";

                            for (n = 0; n < RxDataLen; n++)
                            {
                                StrBuf += RxData[n].ToString("X2") + " ";
                            }
                            string prueba = "";
                            for (int j = 0; j < RxData.Length; j++)
                            {
                                prueba += RxData[j].ToString("X2") + " "; ;
                            }
                            Console.WriteLine(prueba);
                            //  Console.WriteLine("" + St0+" "+St1+ " "+St2 +" "+TxData[4]) ;
                            Console.WriteLine(StrBuf);
                            Console.WriteLine("Read Block Data Error", "Read Block Data");
                        }

                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Read Block Data" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Read Block Data");
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
            }
        }
        public void MiReadLock(string password, byte sector)
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x60;
                Pm = 0x33;
                St0 = St1 = St2 = 0;

                TxData[0] = 0x0;
                TxData[1] = 0xB0;  //Read
                TxData[2] = sector;// Sector Number  
                TxData[3] = (byte)0x00;//Start Block
                TxData[4] = 0x4;  //Block Numbers
                TxDataLen = 5;
                RxDataLen = 0;
                //MiCheckPassword("C9 65 4F 67 C9 65");
                MiCheckPassword(password, sector);
                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {


                        if (RxData[RxDataLen - 2] == 0x90 && RxData[RxDataLen - 1] == 0x00)   //last two Byte(SW1 SW2) is "9000"
                        {
                            int n;
                            string StrBuf = "";

                            for (n = 0; n < 16; n++)
                            {
                                StrBuf += RxData[n].ToString("X2") + " ";
                                Console.WriteLine(StrBuf);
                            }

                            Console.WriteLine(StrBuf);
                            Console.WriteLine("sector: " + sector + ", Read Block Data Successed", "Read Block Data");
                        }
                        else
                        {
                            int n;
                            string StrBuf = "";

                            for (n = 0; n < RxDataLen; n++)
                            {
                                StrBuf += RxData[n].ToString("X2") + " ";
                            }
                            string prueba = "";
                            for (int j = 0; j < RxData.Length; j++)
                            {
                                prueba += RxData[j].ToString("X2") + " "; ;
                            }
                            Console.WriteLine(prueba);
                            //  Console.WriteLine("" + St0+" "+St1+ " "+St2 +" "+TxData[4]) ;
                            Console.WriteLine(StrBuf);
                            Console.WriteLine("Read Block Data Error", "Read Block Data");
                        }

                    }
                    else if ((ReType == 0x4e))
                    {

                        Console.WriteLine("Read Block Data" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Read Block Data");
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
            }
        }

        private void MiWriteBlockBtn_Click(object sender, EventArgs e)
        {
            if (Hdle != 0)
            {
                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                Cm = 0x60;
                Pm = 0x33;
                St0 = St1 = St2 = 0;

                TxData[0] = 0x0;
                TxData[1] = 0xD1;  //Write
                TxData[2] = (byte)0x01;// Sector Number  
                TxData[3] = (byte)0x01;//Start Block
                TxData[4] = 0x1;  //Block Numbers

                //Tesa tesa = new Tesa();
                // string data = tesa.CheckIn("", "", "", "", "", "", "");

                //for (int n = 0; n < 16; n++)
                //    TxData[5 + n] = 0xff;  //16 Bytes Data


                TxDataLen = 21;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {
                        if (RxData[RxDataLen - 2] == 0x90 && RxData[RxDataLen - 1] == 0x00)   //last two Byte(SW1 SW2) is "9000"
                        {
                            Console.WriteLine("Write Block Data Successed", "Write Block Data");
                        }
                        else
                        {
                            Console.WriteLine(RxData[0] + " " + RxData[1]);
                            Console.WriteLine("Write Block Data Error", "Write Block Data");
                        }

                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Write Block Datad ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Write Block Data");
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
            }
        }
        public void changePass(byte sector,byte StartBloq,string password)
        {
            if (Hdle != 0)
            {

                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                MiCheckPassword(password, sector);
                Cm = 0x60;
                Pm = 0x33;
                St0 = St1 = St2 = 0;
                TxData[0] = 0x0;
                TxData[1] = 0xD1;  //Write
                TxData[2] = sector;// Sector Number  
                TxData[3] = StartBloq;//Start Block
                TxData[4] = 0x1;  //Block Numbers

                //HAY QUE OBTENER PRIMERO EL SECTOR DE DICHA TARJETA PARA CAMBIARLE DE UNA LOS 6 PRIMEROS BYTES Y LOS 6 ULTIMOS DEJANDO LOS DE EN MEDIO.

                TxData[5 + 0] = 0x39;
                TxData[5 + 1] = 0xF4;
                TxData[5 + 2] = 0x68;
                TxData[5 + 3] = 0xD9;
                TxData[5 + 4] = 0x27;
                TxData[5 + 5] = 0x4B;

                TxData[5 + 6] = 0xFF;
                TxData[5 + 7] = 0x07;
                TxData[5 + 8] = 0x80;
                TxData[5 + 9] = 0x69;

                TxData[5 + 10] = 0x00;
                TxData[5 + 11] = 0x00;
                TxData[5 + 12] = 0x01;
                TxData[5 + 13] = 0x3B;
                TxData[5 + 14] = 0x0E;
                TxData[5 + 15] = 0xD0;

                TxDataLen = 21;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {

                        if (RxData[RxDataLen - 2] == 0x90 && RxData[RxDataLen - 1] == 0x00)   //last two Byte(SW1 SW2) is "9000"
                        {

                            Console.WriteLine("Write Block Data Successed", "Write Block Data");
                        }
                        else
                        {
                            Console.WriteLine(RxData[0] + " " + RxData[1]);
                            Console.WriteLine("Write Block Data Error", "Write Block Data");
                        }

                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Write Block Datad ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Write Block Data");
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
            }
        }
      

        public void MiWriteBlock(string password, byte sector, string card, byte StartBloq, byte[] data)
        {
            if (Hdle != 0)
            {

                byte Addr;
                byte Cm, Pm;
                UInt16 TxDataLen, RxDataLen;
                byte[] TxData = new byte[1024];
                byte[] RxData = new byte[1024];
                byte ReType = 0;
                byte St0, St1, St2;

                MiCheckPassword(password, sector);
                Cm = 0x60;
                Pm = 0x33;
                St0 = St1 = St2 = 0;
                TxData[0] = 0x0;
                TxData[1] = 0xD1;  //Write
                TxData[2] = sector;// Sector Number  
                TxData[3] = StartBloq;//Start Block
                TxData[4] = 0x1;  //Block Numbers

                int startIndex = 0;
                //HAY QUE AVERGIGUAR EL PORQUÉ DE ESTO
                //if (sector == 0x01 && StartBloq == 0x00)
                //{
                //    startIndex = 7;
                //    TxData[5 + 0] = 0x98;
                //    TxData[5 + 1] = 0x1E;
                //    TxData[5 + 2] = 0x3B;
                //    TxData[5 + 3] = 0xD7;
                //    TxData[5 + 4] = 0x6B;
                //    TxData[5 + 5] = 0x76;
                //    TxData[5 + 6] = 0xFF;
                //}
                //for (int n = startIndex; n < 16; n++)
                //{
                //    //98 1E 3B D7 6B 76 FF
                //    TxData[5 + n] = data[n];  //16 Bytes Data
                //}

                for (int n = startIndex; n < 16; n++)
                {
                 
                    TxData[5 + n] = data[n];  //16 Bytes Data
                }

                TxDataLen = 21;
                RxDataLen = 0;

                Addr = (byte)(byte.Parse("00", NumberStyles.Number));
                int i = ExecuteCommand(Hdle, Addr, Cm, Pm, TxDataLen, TxData, ref ReType, ref St0, ref St1, ref St2, ref RxDataLen, RxData);
                if (i == 0)
                {
                    if (ReType == 0x50)
                    {

                        if (RxData[RxDataLen - 2] == 0x90 && RxData[RxDataLen - 1] == 0x00)   //last two Byte(SW1 SW2) is "9000"
                        {

                            Console.WriteLine("Write Block Data Successed", "Write Block Data");
                        }
                        else
                        {
                            Console.WriteLine(RxData[0] + " " + RxData[1]);
                            Console.WriteLine("Write Block Data Error", "Write Block Data");
                        }

                    }
                    else if ((ReType == 0x4e))
                    {
                        Console.WriteLine("Write Block Datad ERROR" + "\r\n" + "Error Code:  " + (char)St1 + (char)St2, "Write Block Data");
                    }
                    else
                    {
                        Console.WriteLine("Communication Error", "Caution");
                    }
                }
                else
                {
                    Console.WriteLine("Communication Error", "Caution");
                }
            }
            else
            {
                Console.WriteLine("Communication Error", "Caution");
            }
        }

    }
}
