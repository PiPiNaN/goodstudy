import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class HanziService {
  constructor(private http: HttpClient) { }

  getHanzi(id:number){
      return this.http.get(`http://192.168.1.47:5000/api/hanzi/${id}`);
  }

  getPinyin(hanzi:string){
    return this.http.get(`http://192.168.1.47:5000/api/pinyin/${hanzi}`)
  }
}