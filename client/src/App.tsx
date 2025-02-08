import React from 'react';
import { Route, BrowserRouter, Routes } from "react-router-dom";
import Filtragem from './pages/Filtragem/Filtragem';
import Home from './pages/Home/Home';
import SobreNos from './pages/SobreNos/SobreNos';
import SobreProjeto from './pages/SobreProjeto/SobreProjeto';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={Home} />
        <Route path="/Filtragem" Component={Filtragem} />
        <Route path="/SobreNos" Component={SobreNos} />
        <Route path="/SobreProjeto" Component={SobreProjeto} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;