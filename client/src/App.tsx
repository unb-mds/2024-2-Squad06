import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Gastos from './pages/Gastos/Gastos';
import Filtragem from './pages/Filtragem/Filtragem';
import Home from './pages/Home/Home';
import SobreNos from './pages/SobreNos/SobreNos';
import SobreProjeto from './pages/SobreProjeto/SobreProjeto';
import Monitoramento from './pages/Monitoramento/Moitoramento';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Filtragem" element={<Filtragem />} />
        <Route path="/SobreNos" element={<SobreNos />} />
        <Route path="/SobreProjeto" element={<SobreProjeto />} />
        <Route path="/Monitoramento" element={<Monitoramento />} />
        <Route path="/Gastos" element={<Gastos />} />
      </Routes>
    </Router>
  );
}

export default App;