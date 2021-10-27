program main
    use, intrinsic :: iso_c_binding
    implicit none

    interface
        subroutine print_address(ad) bind(c)
            use, intrinsic :: iso_c_binding
            integer(c_int) :: ad
        end subroutine
    end interface

    integer, target :: i =1
    integer, pointer :: ip => null()

    call print_address(i)
    call print_address(ip)

    ip => i
    call print_address(ip)
    
end program main