import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HanziComponent } from "./hanzi/hanzi.component";

const routes: Routes = [
  {path:'hanzi', component: HanziComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
