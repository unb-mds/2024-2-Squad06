import axios from "axios";
import { Diario } from "../models/Diario";
import { Fornecedor } from "../models/Fornecedor";

export const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});

export const fetchDiarios = async (): Promise<Diario[]> => {
  const response = await api.get<Diario[]>("/get-diarios/");
  return response.data;
};

export const fetchSuppliers = async (): Promise<Fornecedor[]> => {
  const response = await api.get<Fornecedor[]>("/fornecedores/");
  return response.data;
};

export const fetchFornecedorByName = async (
  nome: string
): Promise<{ id: number }> => {
  const response = await api.post<{ id: number }>("/fornecedor/", { nome });
  return response.data;
};

export const fetchDiariosPorFornecedor = async (
  id: number,
  filters: {
    nome?: string;
    data_publicacao?: string;
    data_assinatura?: string;
    page: number;
  }
): Promise<Diario[]> => {
  const response = await api.post<Diario[]>(
    `/diarios-fornecedor/${id}/`,
    filters
  );
  return response.data;
};
