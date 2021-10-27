program main
    use array2d_mod
    implicit none
    integer, dimension(2,3) :: a
    integer :: i, j

    do j = 1, 3
        do i = 1, 2
            a(i, j) = i + j
        end do
    end do

    call array2d(a)
    
end program main
