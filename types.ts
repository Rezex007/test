
export type Status = 'Sold' | 'Unsold' | 'Refunded' | 'Pending-Refund';

export type EmailStep = 'Ready' | 'Login-Pending' | 'OTP-Waiting' | 'Purchasing' | 'Success' | 'Returning' | 'Returned';

export interface InventoryItem {
  id: string;
  robloxId: string;
  robloxPass: string;
  status: Status;
  cost: number;
  price: number;
  robuxAmount: number;
  updatedAt: string;
  emailUsed?: string;
  cardUsed?: string;
  refundReason?: string;
}

export interface PaymentInfo {
  id: string;
  cardName: string;
  cardNumber: string;
  expiry: string;
  cvv: string;
}

export interface EmailTracking {
  id: string;
  email: string;
  usagePercent: number;
  currentStep: EmailStep;
  robuxStatus: string;
  cookies?: string;
  lastFetch?: string;
}

export interface EmailLog {
  id: string;
  created_at: string;
  subject: string;
  snippet: string;
  status: string;
  account_id: string;
  otp_code?: string;
  body_html?: string;
}

export interface AppState {
  inventory: InventoryItem[];
  payments: PaymentInfo[];
  emails: EmailTracking[];
  logs: EmailLog[];
}
