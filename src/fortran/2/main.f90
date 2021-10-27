program main
    use minus_array_f_mod
    implicit none
    integer :: i,j,k
    integer, dimension(1:3) :: ii, jj, kk

    ii = [1, 2, 3]
    jj = [2, 3, 4]

    call minus_array(ii, jj, kk)
    print *, kk

    print *, minus_array2(ii, jj)

end program main