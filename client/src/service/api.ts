import axios from "axios";
import { Diario } from "../models/Diario";

export const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});

export const fetchDiarios = async (): Promise<Diario[]> => {
  const response = await api.get<Diario[]>("/get-diarios/");
  return response.data;
};
