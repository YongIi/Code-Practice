module array2d_mod
    interface
        module subroutine array2d(a)
            implicit none
            integer, dimension(:,:), intent(inout) :: a
        end subroutine array2d
    end interface
end module array2d_mod