import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import './Gastos.css';

function Gastos() {
    return (
      <div>
        <Header/>
        <div className="Gastos">
          <div>
            <h1>O que são Gastos públicos ?</h1>
            <p>
                Gastos públicos referem-se ao dinheiro que o governo utiliza para financiar as suas atividades, como a prestação de serviços públicos (saúde, educação, segurança), infraestrutura, investimentos em projetos sociais e o pagamento de dívidas. 
                Esses gastos são realizados com recursos obtidos por meio da arrecadação de impostos, taxas e contribuições, e são essenciais para garantir o funcionamento do Estado e o bem-estar da sociedade.
            </p>
          </div>
          <div>
            <h1>Pontos Importantes</h1>
            <ul>
                <li><strong>Transparência:</strong> A população deve exigir clareza na gestão dos recursos públicos para garantir eficiência e evitar desperdícios.</li>
                <li><strong>Impostos:</strong> Os impostos pagos pela sociedade financiam os serviços públicos, por isso, é importante entender como o governo utiliza esse dinheiro.</li>
                <li><strong>Orçamento e Prioridades:</strong> O governo define suas prioridades no orçamento, e é essencial que a população compreenda onde o dinheiro será investido.</li>
                <li><strong>Dívidas públicas:</strong> Parte dos gastos é destinada ao pagamento de dívidas, o que pode impactar outras áreas e políticas fiscais.</li>
                <li><strong>Participação cidadã:</strong> A população pode influenciar nas decisões sobre o uso dos recursos públicos, garantindo um uso responsável e eficaz do dinheiro arrecadado.</li>
            </ul>
          </div>
        </div>
        <Footer/>
      </div>
    );
  }

  export default Gastos;