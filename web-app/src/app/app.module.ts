import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule} from "@angular/forms";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HanziComponent } from './hanzi/hanzi.component';
import { HanziService } from "./hanzi/hanzi.service";

@NgModule({
  declarations: [
    AppComponent,
    HanziComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    HanziService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
