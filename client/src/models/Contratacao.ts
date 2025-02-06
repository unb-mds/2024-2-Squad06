export interface Contratacao {
  id: number;
  nome: string;
  cnpj: string;
  valor_mensal: string;
  valor_anual: string;
  data_assinatura: string;
  vigencia: string | null;
}
