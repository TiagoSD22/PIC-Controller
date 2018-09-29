# PIC-Controller
Controle de video game feito com microcontrolador PIC18F4520

Este projeto é um protótipo simples de um controle de vídeo game com 4 botes direcionais (cima,baixo,esquerda,direita),
4 botões de ação(A,B,Y,X), 2 gatilhos (Rt,Lt) e 2 bumpers (Rb,Lb), start e select. Foi implementado em um microcontrolador(MCU)
PIC18F4520, os sinais dos botões são enviados para o MCU que interpreta e manda serialmente para um módulo bluetooth HC05. 
Pode funcionar com um PC conectando a este outro módulo bluetooth que receba o sinal e envie para um adpatador serial - usb
conectado à uma entrada USB do PC, para os comando serem reconhecidos como entradas de um teclado, há um programa com interface 
gráfica feito em python usando o módulo pySerial que permite atribuir teclas de atalho aos botões do controle, fazendo com que 
este funcione como um dispositivo HID. O programa converte os sinais em códigos que podem ser entendidos por jogos que 
utilizem directX com versão <= 11.0.
