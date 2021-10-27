module fToCPP
    implicit none

contains

    function add(a, b) result(c) &
        bind(c, name='add')
        use, intrinsic :: iso_c_binding
        integer, intent(in) :: a,b
        integer :: c
        c = a + b
    end function add

end module fToCPP