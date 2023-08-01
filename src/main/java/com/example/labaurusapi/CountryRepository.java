package com.example.labaurusapi;

import java.util.List;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.example.labaurusapi.model.Country;

@RepositoryRestResource(collectionResourceRel = "countries",path = "country")
public interface CountryRepository extends PagingAndSortingRepository<Country, String> {

    List<Country> findByName(@Param("name") String name);
    Country findById(@Param("id") String id);

}
