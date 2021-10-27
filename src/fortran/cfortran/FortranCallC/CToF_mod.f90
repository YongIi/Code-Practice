module CToF_mod
    implicit none

    interface
        function add(a, b) result(c) bind(c, name = 'add')  !"name = 'add'" can be omitted
            use, intrinsic :: iso_c_binding     !Fixed format
            implicit none
            real(c_double) :: a, b, c       !c_double: C的double类型
        end function add

    end interface

end module CToF_mod