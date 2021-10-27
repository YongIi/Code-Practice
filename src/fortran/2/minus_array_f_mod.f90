module minus_array_f_mod
    implicit none

    interface
    subroutine minus_array(a, b, c)
        integer, dimension(1:3), intent(in) :: a, b
        integer, dimension(1:3), intent(out) :: c
    end subroutine minus_array
    end interface

contains
    function minus_array2(a, b) result(c)
        integer, dimension(1:3), intent(in) :: a, b
        integer, dimension(1:3) :: c
        c = a - b
    end function minus_array2

end module minus_array_f_mod