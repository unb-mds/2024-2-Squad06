import React from 'react';

interface LoadingModalProps {
  message?: string;
}

const LoadingModal: React.FC<LoadingModalProps> = ({ message = "Buscando diários..." }) => {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 flex flex-col items-center">
        <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-500"></div>
        <span className="mt-4 text-2xl font-bold" style={{ color: "#112632" }}>
          {message}
        </span>
      </div>
    </div>
  );
};

export default LoadingModal;
