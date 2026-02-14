
-- ตารางเก็บข้อมูลบัญชีอีเมลและคุกกี้
CREATE TABLE emails (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cookies TEXT, -- เก็บ JSON string ของ cookies (ควร Encrypt เพิ่มเติม)
    usage_percent INTEGER DEFAULT 0,
    current_step TEXT DEFAULT 'Ready',
    robux_status TEXT,
    last_fetch TIMESTAMP WITH TIME ZONE
);

-- ตารางเก็บ Logs ที่ดึงมาได้
CREATE TABLE email_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    subject TEXT NOT NULL,
    snippet TEXT,
    status TEXT DEFAULT 'pending', -- 'pending', 'used', 'expired'
    account_id TEXT NOT NULL REFERENCES emails(email) ON DELETE CASCADE,
    otp_code VARCHAR(10) -- สกัดรหัสมาเก็บไว้เลย
);

-- เพิ่ม Index
CREATE INDEX idx_emails_status ON emails(current_step);
CREATE INDEX idx_logs_otp ON email_logs(otp_code);
