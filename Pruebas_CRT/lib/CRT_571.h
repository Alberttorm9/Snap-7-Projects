#define ERR		-1
#define OK		0

#define PAC_ADDRESS	1021

#define ENQ  0x05//��������ͨ����·(ѯ��).
#define ACK  0x06//ȷ��(����).
#define NAK  0x15//ͨ��æ.

/* Data structure for reply message	
	//replyType=0x50     PositiveReply
	//replyType=0x4e     NegativeReply   
	//replyType=0x10     ReplyReceivingFailure
	//replyType=0x20     CommandCancellation
	//replyType=0x30     ReplyTimeout
*/
HANDLE APIENTRY CommOpen(char *Port);
int APIENTRY CommSetting(HANDLE ComHandle,char *ComSeting);
HANDLE APIENTRY CommOpenWithBaut(char *Port, unsigned int Baudrate);
int APIENTRY CommClose(HANDLE ComHandle);
int APIENTRY ExecuteCommand(HANDLE ComHandle,BYTE TxAddr,BYTE TxCmCode,BYTE TxPmCode,int TxDataLen,BYTE TxData[],BYTE *RxReplyType,BYTE *RxStCode0,BYTE *RxStCode1,BYTE *RxStCode2,int *RxDataLen,BYTE RxData[]);
int APIENTRY ICCardTransmit(HANDLE ComHandle,BYTE TxAddr,BYTE TxCmCode,BYTE TxPmCode,int TxDataLen,BYTE TxData[],BYTE *RxReplyType,BYTE *RxCmCode,BYTE *RxPmCode,BYTE *RxStCode0,BYTE *RxStCode1,BYTE *RxStCode2,int *RxDataLen,BYTE RxData[]);

