.global _start
.text
;# Convert int value to string
;# rdi - Pointer to the end of output buffer
;# rsi - Int value to write
;# rax - Returns address of string start
write_int_to_string:
  dec %rdi
  movb $0x0A, (%rdi)    ;# Write '\n'
  movq %rsi, %rax
  movq $10, %rcx
 to_str_loop:
  dec %rdi              ;# buffer_pointer--
  xorq %rdx, %rdx       ;# rdx = 0
  divq %rcx             ;# q,r = rax / rcx
  addq $0x30, %rdx      ;# rdx = char(rdx)
  movb %dl, (%rdi)      ;# *buffer_pointer = char(rdx)
  cmp $0x0, %rax        ;# while q != 0
  jne to_str_loop
  movq %rdi, %rax
  ret


;# Print output buffer
;# rdi - Pointer to start of string
print_ans:
  ;# sys_write
  movq %rdi, %rsi
  movq $1, %rax
  movq $1, %rdi
  leaq end_ans_buffer, %rdx
  subq %rsi, %rdx
  syscall
  ret


;# Exit program
exit:
  ;# sys_exit
  movq $60, %rax
  xorq %rdi, %rdi
  syscall


;# 
;# MAIN
;#
_start:

  movq $0, %r15         ;# ans = 0
  leaq input, %r14      ;# input_ptr

 loop:
  cmp $end_input, %r14
  jl not_end
  ;# str = write_int_to_string(end_ans_buffer, ans)
  leaq end_ans_buffer, %rdi
  movq %r15, %rsi
  call write_int_to_string
  movq %rax, %rdi
  ;# print_ans(str)
  call print_ans
  ;# exit()
  call exit

 not_end:

  ;# SOLUTION HERE
  movb (%r14), %al
  subq $0x30, %rax
  addq %rax, %r15
  inc %r14
  jmp loop

.data
ans_buffer: .ascii "                    "
end_ans_buffer:
input: .ascii "INPUT_GOES_HERE"
end_input:
