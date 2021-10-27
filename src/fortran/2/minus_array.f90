subroutine minus_array(a, b, c)
    integer, dimension(1:3), intent(in) :: a, b
    integer, dimension(1:3), intent(out) :: c
    c = a - b
end subroutine minus_array