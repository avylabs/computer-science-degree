package com.avelatte.baozi_api_rest.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode
public class Produto {
    
    @Id
    private Long id;
    private String nome;
    private BigDecimal preco;
    private boolean estoque;

}