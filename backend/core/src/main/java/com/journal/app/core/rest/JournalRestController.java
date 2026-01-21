package com.journal.app.core.rest;


import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/days", produces = MediaType.APPLICATION_JSON_VALUE)
public class JournalRestController {

    @GetMapping
    public String getHelloWorld(){
        return "Hello World";
    }

}
