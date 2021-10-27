program main
    use CToF_mod
    implicit none
    real(8) :: x,y,z

    x = 5.0_8; y = 4.1_8

    z = add(x, y)
    
    print *, z
    
end program main