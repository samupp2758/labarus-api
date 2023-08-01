package com.example.labaurusapi.controller;

import com.example.labaurusapi.model.Country;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CountryController {

    @GetMapping
    public Country getCountry(){
        return null;
    }
}
