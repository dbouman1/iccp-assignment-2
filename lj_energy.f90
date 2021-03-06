subroutine func(pos,candidate_pos,N_candidates,N_existing,sigma_squared,epsilon,bend_energy,last_angle,possib_angles,energies)
    implicit none
    
    integer, intent(in) :: N_candidates, N_existing
    real(8), intent(in) :: sigma_squared, epsilon, last_angle, bend_energy
    real(8), dimension(N_existing,2), intent(in) :: pos
    real(8), dimension(N_candidates,2), intent(in) :: candidate_pos
    real(8), dimension(N_candidates), intent(in) :: possib_angles
    
    real(8), dimension(N_candidates), intent(out) :: energies
    
    real(8) :: V, pi, abs_distance_squared
    integer :: i,j
    
    pi = 3.1415927
    
    do i=1,N_candidates
        do j=1,N_existing-1
            abs_distance_squared = sum((candidate_pos(i,:) - pos(j,:))**2) / sigma_squared
            V = 4*epsilon*( (abs_distance_squared)**(-6) - (abs_distance_squared)**(-3))
            energies(i) = energies(i)+V
        end do
        energies(i) = energies(i)+bend_energy*sin(0.5*modulo( (possib_angles(i)-last_angle),pi) )**2
    end do
    
end subroutine