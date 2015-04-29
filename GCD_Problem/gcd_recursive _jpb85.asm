	# Main program reads in two ints calls function prints result
	.text             
	.globl  main  
main:
    li $v0,4         #print prompt 
    la $a0,prompt
    syscall

    li $v0,5        #read first argument
    syscall
    move $t0,$v0
	
	li $v0,4         #print prompt 
    la $a0,prompt  
    syscall

    li $v0,5   #read second argument
    syscall
    move $a1,$v0

    li $v0,4  #print a_is
    la $a0,a_is
    syscall

    move $a0,$t0 #print a
    li $v0,1
    syscall
    
    li $v0,4  #print b_is
    la $a0,b_is
    syscall

    move $a0,$a1 #print b
    li $v0,1
    syscall

    li $v0,4   #print result
    la $a0,result
    syscall

	move $a0,$t0 #move a

    move $v1,$ra #save address
    jal gcd
	
    move $ra,$v1 #restore address
    
    move $a0,$v0  #print gcd
    li $v0,1
    syscall

    jr $ra #end

gcd:
    beq $a1,$zero,end #if b = zero go to end

    sub $sp,$sp,4  #stack address
    sw $ra,0($sp)

    move $t0,$a1 #temp = b
    rem $a1,$a0,$a1   #b = a%b
    move $a0,$t0 #a =b b
    jal gcd   #jump and link

    lw $ra,0($sp)  #getting address
    add $sp,$sp,4
    jr $ra  #return

end:
    move $v0,$a0 
	jr	$ra

.data
prompt:
    .asciiz "Please enter a positive integer (type number press enter):\n"
a_is:
    .asciiz "\n a = "
b_is:
    .asciiz "\n b = "
result:
    .asciiz "\nGCD is "

