package com.avelatte.baozi_api_rest.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.avelatte.baozi_api_rest.models.Cliente;

public interface ClienteRepository extends JpaRepository<Cliente, Long> {
    
}
