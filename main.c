#include<delays.h>
#include<math.h>
#include<usart.h>
#include<p18f4520.h>

#pragma config OSC      = INTIO67
#pragma config WDT      = OFF, MCLRE = OFF         
#pragma config DEBUG    = ON, LVP = OFF, PWRT = ON 
#pragma config PBADEN   = OFF 

#define CIMA PORTAbits.RA0
#define DIREITA PORTAbits.RA1
#define BAIXO PORTAbits.RA2
#define ESQUERDA PORTAbits.RA3
#define ACAO1 PORTAbits.RA4
#define ACAO2 PORTAbits.RA5
#define ACAO3 PORTAbits.RA6
#define ACAO4 PORTAbits.RA7
#define START PORTBbits.RB0
#define BACK PORTBbits.RB1
#define GATILHOD PORTBbits.RB2
#define GATILHOE PORTBbits.RB3
#define BUMPERD PORTBbits.RB4
#define BUMPERE PORTBbits.RB5
#define MODO PORTBbits.RB6

short direita_pressionado,esquerda_pressionado,cima_pressionado,baixo_pressionado;
short acao1_pressionado,acao2_pressionado,acao3_pressionado,acao4_pressionado;
short gatilhod_pressionado,gatilhoe_pressionado,bumperd_pressionado,bumpere_pressionado;

void Debounce(void){
	Delay10KTCYx(35);
}

void Configurar_PIC(void){
	ADCON1 = 0x0F;
	OSCCON = 0x70;

	TRISA = 0b11111111;
	TRISB = 0b01111111;
	TRISC = 0b10000000;
	TRISD = 0b00000000;
	TRISE = 0b00000000;
	
	LATA = 0b00000000;
	LATB = 0b00000000;
	LATC = 0b00000000;
	LATD = 0b00000000;
	LATE = 0b00000000;

	OpenUSART(USART_TX_INT_OFF
			 &USART_RX_INT_OFF
			 &USART_ASYNCH_MODE
			 &USART_EIGHT_BIT
			 &USART_BRGH_HIGH,51);//FOSC/(16 * baud) - 1
		
}

void Parear_Bluetooth(void){
	long i;
	Delay10KTCYx(1000);
	putrsUSART("AT+INQ\r\n");
	for(i = 0; i < 600000; i++){}
	putrsUSART("AT+CONN1\r\n");
}

void Modo_PC(void){
	if(CIMA){
		cima_pressionado = 1;
		putcUSART('w');
		Debounce();
	}
	else{
		if(cima_pressionado){
			cima_pressionado = 0;
			putcUSART('W');
			LATCbits.LATC0 = 0;
		}
	}
	if(DIREITA){
		direita_pressionado = 1;
		putcUSART('d');
		Debounce();
	}
	else{
		if(direita_pressionado){
			direita_pressionado = 0;
			putcUSART('D');
		}
	}
	if(BAIXO){
		baixo_pressionado = 1;
		putcUSART('s');
		Debounce();
	}
	else{
		if(baixo_pressionado){
			baixo_pressionado = 0;
			putcUSART('S');
		}
	}
	if(ESQUERDA){
		esquerda_pressionado = 1;
		putcUSART('a');
		Debounce();
	}
	else{
		if(esquerda_pressionado){
			esquerda_pressionado = 0;
			putcUSART('A');
		}
	}
	if(ACAO1){
		acao1_pressionado = 1;
		putcUSART('u');
		Debounce();
	}
	else{
		if(acao1_pressionado){
			acao1_pressionado = 0;
			putcUSART('U');
		}
	}
	if(ACAO2){
		acao2_pressionado = 1;
		putcUSART('k');
		Debounce();
	}
	else{
		if(acao2_pressionado){
			acao2_pressionado = 0;
			putcUSART('K');
		}
	}
	if(ACAO3){
		acao3_pressionado = 1;
		putcUSART('j');
		Debounce();
	}
	else{
		if(acao3_pressionado){
			acao3_pressionado = 0;
			putcUSART('J');
		}
	}
	if(ACAO4){
		acao4_pressionado = 1;
		putcUSART('h');
		Debounce();
	}
	else{
		if(acao4_pressionado){
			acao4_pressionado = 0;
			putcUSART('H');
		}
	}
	if(GATILHOD){
		gatilhod_pressionado = 1;
		putcUSART('v');
		Debounce();
	}
	else{
		if(gatilhod_pressionado){
			gatilhod_pressionado = 0;
			putcUSART('V');
		}
	}
	if(GATILHOE){
		gatilhoe_pressionado = 1;
		putcUSART('z');
		Debounce();
	}
	else{
		if(gatilhoe_pressionado){
			gatilhoe_pressionado = 0;
			putcUSART('Z');
		}
	}
	if(BUMPERD){
		bumperd_pressionado = 1;
		putcUSART('c');
		Debounce();
	}
	else{
		if(bumperd_pressionado){
			bumperd_pressionado = 0;
			putcUSART('C');
		}
	}
	if(BUMPERE){
		bumpere_pressionado = 1;
		putcUSART('x');
		Debounce();
	}
	else{
		if(bumpere_pressionado){
			bumpere_pressionado = 0;
			putcUSART('X');
		}
	}
	if(START){
		putcUSART('p');
		Debounce();
	}
	if(BACK){
		putcUSART('b');
		Debounce();
	}
}

void Modo_Mini_Game(void){
	if(CIMA){
		putcUSART('w');
		Debounce();
	}
	if(DIREITA){
		putcUSART('d');
		Debounce();
	}
	if(BAIXO){
		putcUSART('s');
		Debounce();
	}
	if(ESQUERDA){
		putcUSART('a');
		Debounce();
	}
	if(START){
		putcUSART('p');
		Debounce();
	}
	if(BACK){
		putcUSART('b');
		Debounce();
	}
}

void main(void){
	direita_pressionado = 0;
	esquerda_pressionado = 0;
	cima_pressionado = 0;
	baixo_pressionado = 0;
	acao1_pressionado = 0;
	acao2_pressionado = 0;
	acao3_pressionado = 0;
	acao4_pressionado = 0;
	gatilhod_pressionado = 0;
	gatilhoe_pressionado = 0;
	bumperd_pressionado = 0;
	bumpere_pressionado = 0;
	Configurar_PIC();
	Parear_Bluetooth();
	while(1){
		if(MODO == 1){
			Modo_PC();
		}
		else{
			Modo_Mini_Game();
		}
	}
}