import { Contratacao } from "./Contratacao";

export interface Diario {
  id?: number;
  data_publicacao?: string;
  url?: string;
  txt_url?: string;
  excerpts?: string;
  contratacoes?: Contratacao[];
}
