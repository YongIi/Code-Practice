submodule(array2d_mod) array2d_smod
contains
    module procedure array2d
        integer :: i, rows

        rows = size(a,1)
        
        do i = 1, rows
            print *, a(i, :)
        end do

        return

    end procedure array2d
end submodule