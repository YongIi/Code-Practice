program main
    use exampleFuncs_mod
    implicit none
    
    procedure(func_t), pointer :: f_ptr => null()

    real :: input

    write (*,*) "Enter a value: "
    read (*,*) input

    if (input < 0) then
        f_ptr => f1
    else
        f_ptr => f2
    end if

    write (*,*) "double value: ", f_ptr(input)
    
end program main