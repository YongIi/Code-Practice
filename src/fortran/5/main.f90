program main
    use point_class
    implicit none

    type(point_t) :: xp1, xp2, xp3

    xp1 = point_t(2.1, 5.0)
    xp2 = point_t(3.9, 2.0)
    
    xp3 = addTwoPoints(xp1, xp2)

    print *, xp3%x_, xp3%y_

end program main