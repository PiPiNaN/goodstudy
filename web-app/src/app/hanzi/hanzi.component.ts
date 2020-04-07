import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HanziService } from "./hanzi.service";
import HanziWriter from 'hanzi-writer';
import { Hanzi } from "./hanzi";

@Component({
  selector: 'app-hanzi',
  templateUrl: './hanzi.component.html',
  styleUrls: ['./hanzi.component.css']
})
export class HanziComponent implements OnInit {

  @ViewChild('charactertarget') charatertarget: ElementRef;

  hanzi: Hanzi;
  id: number = 0;
  pinyin:string;
  writer: HanziWriter;
  

  constructor(private hs: HanziService) { }

  ngOnInit(): void {
    this.hs.getHanzi(this.id).subscribe(hanzi => {
      this.hanzi = <Hanzi>hanzi;
      console.log(this.hanzi);
      this.hs.getPinyin(this.hanzi.hanzi).subscribe(p => this.pinyin = p as string);
      this.hanzitest();
    });
  }

  hanzitest() {
    if (!this.writer) {
      this.writer = HanziWriter.create('grid-background-target', this.hanzi.hanzi, {
        width: 400,
        height: 400,
        showCharacter: false,
        showOutline: true,
        showHintAfterMisses: 1,
        highlightOnComplete: true,
        radicalColor: '#168F16', // green
        padding: 10
      });
    } else {
      this.writer.setCharacter(this.hanzi.hanzi);
    }
    this.writer.quiz({
      onComplete: function (summaryData) {
        console.log('You did it! You finished drawing ' + summaryData.character);
        console.log('You made ' + summaryData.totalMistakes + ' total mistakes on this quiz');
        console.log(summaryData);
        //writer2.updateColor('strokeColor', '#AA12CD')        
        // return function () {
        //   this.hanzi.learned += 1;
        //   console.log(this.hanzi);
        // }
      },
    });
  }

  onPre(){
    this.id --;
    this.hs.getHanzi(this.id).subscribe(hanzi => {
      this.hanzi = <Hanzi>hanzi;
      console.log(this.hanzi);
      this.hs.getPinyin(this.hanzi.hanzi).subscribe(p => this.pinyin = p as string);
      this.hanzitest()
    });
  }

  onThis(){
    this.hs.getHanzi(this.id).subscribe(hanzi => {
      this.hanzi = <Hanzi>hanzi;
      console.log(this.hanzi);
      this.hs.getPinyin(this.hanzi.hanzi).subscribe(p => this.pinyin = p as string);
      this.hanzitest()
    });
  }

  onNext() {
    this.id++;
    this.hs.getHanzi(this.id).subscribe(hanzi => {
      this.hanzi = <Hanzi>hanzi;
      console.log(this.hanzi);
      this.hs.getPinyin(this.hanzi.hanzi).subscribe(p => this.pinyin = p as string);
      this.hanzitest()
    });
  }
  onTest() {
    this.hanzitest();
  }
  onAnimation() {
    this.writer.animateCharacter();
  }

}
