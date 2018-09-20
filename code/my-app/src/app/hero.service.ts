import { Injectable } from '@angular/core';
 
import { Observable, of } from 'rxjs';
import { Http , Response } from '@angular/http';

import { Hero } from './hero';
import { HEROES } from './mock-heroes';
import { MessageService } from './message.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators'; 
 
const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};


@Injectable({ providedIn: 'root' })
export class HeroService {


  
  private heroesUrl = 'http://xiencias.com:5500/agentes/';  // URL to web api
 
  constructor(private http: HttpClient,private messageService: MessageService) { }



    getAgentes() {
      return this.http.get(this.heroesUrl);
   }
 
  getHeroes(): Observable<Hero[]> {
    // TODO: send the message _after_ fetching the heroes
    this.messageService.add('HeroService: fetched heroes');
    return of(HEROES);
  }
 
  getHero(id: number): Observable<Hero> {
    // TODO: send the message _after_ fetching the hero
    this.messageService.add(`HeroService: fetched hero id=${id}`);
    return of(HEROES.find(hero => hero.id === id));
  }
}