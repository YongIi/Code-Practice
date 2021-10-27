#define ZERO

program main
    implicit none
    integer, pointer :: pi => NULL(), pi2 => NULL()
    real, pointer :: pr => NULL()
    integer, dimension(:), pointer :: parray => NULL()

    integer, target :: i = 1010

#ifndef ZERO
    print *, "i = ", i
    print *, pi

    pi => i
    print *, "pi = ", pi
#endif

    print *, associated(pi)
    allocate(pi)
    print *, associated(pi)

    pi = 501

    print *, "pi = ", pi
    pi2 => pi
    print *, "pi2 = ", pi2
    
end program main