# SCADA System Simulation and Security Analysis

## 📘 **Overview**
This project simulates a **SCADA (Supervisory Control and Data Acquisition) system** for a **nuclear power plant**. The simulation models the communication between the **SCADA HMI (Human-Machine Interface)** and the plant's control systems using the **Modbus protocol**.  
The primary goal is to **analyze and address security vulnerabilities** by simulating various types of cyberattacks on the system.  

---

## ✨ **Key Features**

### 🔧 **System Simulation**
- **Nuclear Power Plant Model**: Simulates the control of key components such as **control rods** and **water temperature monitoring**.  
- **SCADA HMI Interaction**: Models the interaction between the SCADA HMI and the plant's control systems.  

### ⚠️ **Attack Simulations**
- **Replay Attack**: Captures and replays previously recorded traffic to mislead the system.  
- **Command Injection**: Executes unauthorized commands on the system, enabling attackers to control critical components.  

### 🔗 **Communication Protocol**
- **Modbus Protocol**: Used for system communication.  
- **Message Types**: 
  - **Read** and **Write** requests.  
- **Signal Types**:
  - **Analog Input**: Read-only.  
  - **Analog Output**: Read/Write.  
  - **Digital Input**: Read-only.  
  - **Digital Output**: Read/Write.  

### 🚨 **Alarm System**
- **Water Temperature Monitoring**:  
  - **High Alarm**: Triggers at **350°C** to signal a critical issue.  
  - **Low Alarm**: Triggers at **250°C** to signal a potential risk.  

---

## 🛠️ **Implementation Details**

### **Technologies Used**
- **C# .NET**: Core simulation of the nuclear power plant system.  
- **Python with PyQt5**: Development of the SCADA HMI interface.  
- **Machine Learning**: Attack detection and system response optimization.  

### **Man-in-the-Middle Component**
- Uses the **PyDivert** library to **intercept network packets** and execute attacks on the system.  

---

### 🔐 **Security Improvements**
- **Automation Review**: Review and optimize automation algorithms to improve security and response times.  
- **Advanced Attack Detection**: Enhance the machine learning models to better detect and prevent sophisticated attacks.  


