module add_mod
    implicit none

contains

    subroutine add(a, b, c) bind(c)
        use, intrinsic :: iso_c_binding
        
        integer(c_int), intent(in) :: a, b
        integer(c_int), intent(out) :: c

        c = a + b

    end subroutine add

end module add_mod