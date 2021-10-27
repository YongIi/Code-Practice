module point_class
    implicit none

    type point_t
        real :: x_ = 1.0, y_ =2.0
    end type point_t

contains

    function addTwoPoints(p1, p2) result(p3)
        type(point_t), intent(in) :: p1, p2
        type(point_t) :: p3

        p3%x_ = p1%x_ + p2%x_
        p3%y_ = p1%y_ + p2%y_
    end function addTwoPoints

end module point_class