import React, { useState } from 'react';
import './App.jsx';

export default class APIService{
    // Insert an article
    static search(colors, searchTerms){
        return fetch(`/api/search`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify({ colors, searchTerms })
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}