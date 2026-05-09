package com.avelatte.baozi_api_rest.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode
public class Pedido {

    @Id
    private Long id;
    private Long clienteId;
    private Long produtoId;
    private int quantidade;

}
