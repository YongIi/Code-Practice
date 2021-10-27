module exampleFuncs_mod
    implicit none
    ! def: type of function

    abstract interface

        function func_t(x)
            real :: func_t
            real, intent(in) :: x
        end function func_t

    end interface

contains

    function f1(x)
        real :: f1
        real, intent(in) :: x

        f1 = 2.0 * x
    end function f1

    function f2(x)
        real :: f2
        real, intent(in) :: x

        f2 = - 2.0 * x
    end function f2

end module exampleFuncs_mod