
import React, { useState, useEffect } from 'react';
import { HashRouter, Routes, Route, Link, useLocation } from 'react-router-dom';
import { 
  LayoutDashboard, 
  Package, 
  CreditCard, 
  Mail, 
  Menu, 
  X, 
  TrendingUp, 
  History
} from 'lucide-react';
import Dashboard from './Dashboard';
import Inventory from './Inventory';
import Payment from './Payment';
import EmailTrackingPage from './EmailTracking';
import EmailLogsPage from './EmailLogs';
import AccountLogsPage from './AccountLogs';
import { AppState, InventoryItem, PaymentInfo, EmailTracking, EmailLog } from './types';

const INITIAL_STATE: AppState = {
  inventory: [],
  payments: [],
  emails: [],
  logs: [] // ลบ Mock Logs ออกตามคำขอ
};

const App: React.FC = () => {
  const [state, setState] = useState<AppState>(() => {
    const saved = localStorage.getItem('robux_manager_state_v7');
    return saved ? JSON.parse(saved) : INITIAL_STATE;
  });

  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  useEffect(() => {
    localStorage.setItem('robux_manager_state_v7', JSON.stringify(state));
  }, [state]);

  // ฟังก์ชันสำหรับเพิ่ม Log จากภายนอก (API Simulation)
  useEffect(() => {
    (window as any).addExternalLogs = (newLogs: EmailLog[]) => {
      addLogs(newLogs);
    };
  }, []);

  const addInventory = (newItem: InventoryItem) => setState(prev => ({ ...prev, inventory: [newItem, ...prev.inventory] }));
  const deleteInventory = (id: string) => setState(prev => ({ ...prev, inventory: prev.inventory.filter(i => i.id !== id) }));
  
  const addPayment = (newPay: PaymentInfo) => setState(prev => ({ ...prev, payments: [newPay, ...prev.payments] }));
  const deletePayment = (id: string) => setState(prev => ({ ...prev, payments: prev.payments.filter(p => p.id !== id) }));

  const updateEmail = (updatedEmail: EmailTracking) => {
    setState(prev => ({
      ...prev,
      emails: prev.emails.map(e => e.id === updatedEmail.id ? updatedEmail : e)
    }));
  };
  const addEmail = (newEmail: EmailTracking) => setState(prev => ({ ...prev, emails: [newEmail, ...prev.emails] }));
  const deleteEmail = (id: string) => setState(prev => ({ ...prev, emails: prev.emails.filter(e => e.id !== id) }));

  const addLogs = (newLogs: EmailLog[]) => {
    setState(prev => {
      const existingKeys = new Set(prev.logs.map(l => `${l.account_id}-${l.subject}-${l.created_at}`));
      const uniqueNewLogs = newLogs.filter(l => !existingKeys.has(`${l.account_id}-${l.subject}-${l.created_at}`));
      return {
        ...prev,
        logs: [...uniqueNewLogs, ...prev.logs].sort((a, b) => 
          new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
        )
      };
    });
  };

  return (
    <HashRouter>
      <div className="flex min-h-screen bg-[#09090b] text-zinc-100">
        <aside className={`${isSidebarOpen ? 'w-64' : 'w-20'} transition-all duration-300 border-r border-zinc-800 bg-zinc-950 sticky top-0 h-screen flex flex-col z-40`}>
          <div className="p-6 flex items-center gap-3">
            <div className="bg-emerald-500 p-2 rounded-lg"><TrendingUp className="text-zinc-950 w-6 h-6" /></div>
            {isSidebarOpen && <span className="font-bold text-xl tracking-tight text-white">RobuxPro</span>}
          </div>
          <nav className="flex-1 px-4 space-y-2 mt-4">
            <SidebarLink to="/" icon={<LayoutDashboard size={20} />} label="Dashboard" isOpen={isSidebarOpen} />
            <SidebarLink to="/inventory" icon={<Package size={20} />} label="Stock & Tracking" isOpen={isSidebarOpen} />
            <SidebarLink to="/payment" icon={<CreditCard size={20} />} label="Payments" isOpen={isSidebarOpen} />
            <SidebarLink to="/emails" icon={<Mail size={20} />} label="Email Tracker" isOpen={isSidebarOpen} />
            <SidebarLink to="/logs" icon={<History size={20} />} label="Email Logs" isOpen={isSidebarOpen} />
          </nav>
          <button onClick={() => setIsSidebarOpen(!isSidebarOpen)} className="p-4 border-t border-zinc-800 flex items-center justify-center hover:bg-zinc-900 transition-colors text-zinc-500">
            {isSidebarOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </aside>

        <main className="flex-1 overflow-y-auto p-4 md:p-8">
          <Routes>
            <Route path="/" element={<Dashboard state={state} />} />
            <Route path="/inventory" element={<Inventory items={state.inventory} emails={state.emails} payments={state.payments} onAdd={addInventory} onDelete={deleteInventory} />} />
            <Route path="/payment" element={<Payment items={state.payments} onAdd={addPayment} onDelete={deletePayment} />} />
            <Route path="/emails" element={<EmailTrackingPage items={state.emails} onAdd={addEmail} onUpdate={updateEmail} onDelete={deleteEmail} onAddLogs={addLogs} />} />
            <Route path="/logs" element={<EmailLogsPage logs={state.logs} emails={state.emails} />} />
            <Route path="/logs/:emailId" element={<AccountLogsPage logs={state.logs} />} />
          </Routes>
        </main>
      </div>
    </HashRouter>
  );
};

const SidebarLink: React.FC<{ to: string, icon: React.ReactNode, label: string, isOpen: boolean }> = ({ to, icon, label, isOpen }) => {
  const location = useLocation();
  const isActive = location.pathname.startsWith(to) && (to !== '/' || location.pathname === '/');
  return (
    <Link to={to} className={`flex items-center gap-4 px-4 py-3 rounded-xl transition-all ${isActive ? 'bg-emerald-500/10 text-emerald-500 border border-emerald-500/20' : 'text-zinc-400 hover:bg-zinc-900 hover:text-zinc-100'}`}>
      {icon}{isOpen && <span className="font-medium">{label}</span>}
    </Link>
  );
};

export default App;
