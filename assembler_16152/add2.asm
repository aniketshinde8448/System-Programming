	section .data
	a dd 4
	b dd 3
	msg db "%d",10,0

	section .bss
	c resd 1

	section .text
	global main
	extern printf

main:
	mov eax,a
	mov ebx,b
	add eax,ebx
	push eax
	push msg
	call printf
	add esp,8
