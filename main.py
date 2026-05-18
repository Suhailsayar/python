from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
import os

OUTPUT = "Online_Shopping_System.pdf"

PAGE_W, PAGE_H = A4

# ── page-number callback ──────────────────────────────────────────────────────
def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 10)
    canvas.drawRightString(PAGE_W - 1*inch, 0.5*inch, str(doc.page))
    canvas.restoreState()

doc = BaseDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=1.2*inch,
    leftMargin=1.2*inch,
    topMargin=1*inch,
    bottomMargin=1*inch,
)

frame = Frame(doc.leftMargin, doc.bottomMargin,
              doc.width, doc.height, id='normal')
template = PageTemplate(id='main', frames=frame, onPage=add_page_number)
doc.addPageTemplates([template])

# ── styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

title_style = ParagraphStyle('MyTitle',
    fontName='Times-Bold', fontSize=14,
    alignment=TA_CENTER, spaceAfter=6, leading=20)

center_style = ParagraphStyle('Center',
    fontName='Times-Roman', fontSize=12,
    alignment=TA_CENTER, spaceAfter=4, leading=16)

center_bold = ParagraphStyle('CenterBold',
    fontName='Times-Bold', fontSize=12,
    alignment=TA_CENTER, spaceAfter=4, leading=16)

h1 = ParagraphStyle('H1',
    fontName='Times-Bold', fontSize=13,
    spaceAfter=6, spaceBefore=10, leading=18)

h2 = ParagraphStyle('H2',
    fontName='Times-Bold', fontSize=12,
    spaceAfter=4, spaceBefore=8, leading=16)

h3 = ParagraphStyle('H3',
    fontName='Times-Bold', fontSize=11,
    spaceAfter=3, spaceBefore=6, leading=15)

body = ParagraphStyle('Body',
    fontName='Times-Roman', fontSize=11,
    spaceAfter=4, spaceBefore=2, leading=15, alignment=TA_JUSTIFY)

bullet = ParagraphStyle('Bullet',
    fontName='Times-Roman', fontSize=11,
    spaceAfter=3, spaceBefore=2, leading=15,
    leftIndent=20, bulletIndent=8)

toc_entry = ParagraphStyle('TOC',
    fontName='Times-Roman', fontSize=11,
    spaceAfter=2, leading=15)

toc_bold = ParagraphStyle('TOCBold',
    fontName='Times-Bold', fontSize=11,
    spaceAfter=2, leading=15)

def B(text): return f"<b>{text}</b>"
def bul(text): return Paragraph(f"• {text}", bullet)

story = []

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — Cover
# ══════════════════════════════════════════════════════════════════════════════
story.append(Spacer(1, 1.8*inch))
story.append(Paragraph(B("ONLINE SHOPPING SYSTEM"), title_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph(B("Assignment report"), center_bold))
story.append(Paragraph(B("submitted by"), center_bold))
story.append(Paragraph("SHABROOZA YASEEN (230333)", center_style))
story.append(Paragraph("SANA SHOWKAT (230332)", center_style))
story.append(Spacer(1, 0.6*inch))

# College logo placeholder (simple text box to match visual)
story.append(Spacer(1, 0.3*inch))

story.append(Spacer(1, 0.6*inch))
story.append(Paragraph(B("Department of Computer Science and Engineering"), center_bold))
story.append(Paragraph(B("Government College of Engineering and Technology"), center_bold))
story.append(Paragraph(B("Safapora, Ganderbal"), center_bold))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — Table of Contents
# ══════════════════════════════════════════════════════════════════════════════
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Table of Contents", ParagraphStyle('TOCTitle',
    fontName='Times-Roman', fontSize=14, alignment=TA_CENTER,
    spaceAfter=14, leading=20)))

toc_data = [
    ("Introduction", "5", False),
    ("1.1 Purpose:", "5", False),
    ("1.2 Product Scope:", "5", False),
    ("1.3 Definitions, Acronyms, and Abbreviations", "5", False),
    ("1.4 Technologies to be used", "6", False),
    ("Overall Description", "7", False),
    ("2.1 Product Perspective", "7", False),
    ("2.2  User Characteristics and Classes", "7", False),
    ("User Characteristics", "7", False),
    ("2.3 Classes of Users", "7", False),
    ("2.3.1. Operating Environment", "8", False),
    ("2.3.2 User Documentation", "8", False),
    ("2.3.3  Software Interfaces", "8", False),
    ("2.3.4 Hardware Interfaces", "8", False),
    ("2.3.5 External Forces", "8", False),
    ("2.3.6  Dependencies", "8", False),
    ("2.3.7  Constraints", "9", False),
    ("3.3 System Features", "9", False),
    ("3.3.1 Functional Requirements", "9", False),
    ("3.3.2 Non-Functional Requirements", "9", False),
    ("4 Commitment to delivering a high-quality university website", "10", True),
    ("5 How testing contributes to user satisfaction and operational", "10", True),
    ("ONLINE SHOPPING SYSTEM DESIGN DOCUMENT", "11", True),
    ("5.1 System Design (front-end design)", "11", False),
    ("5.1.1 Use case diagram", "11", False),
    ("5.1.2 Class Diagram", "11", False),
    ("5.1.3 Sequence Diagram", "12", False),
    (". Collaboration DiagramBottom of Form", "12", False),
    ("5.1.4 Data Flow Diagram", "13", False),
    ("5.2 Database Design", "14", False),
    ("5.2.1 ER Diagram", "14", False),
    ("6 Future scope", "15", False),
    ("6. 1. Integration with AI & Machine Learning", "15", False),
    ("6.2 Support for 6G and Future Networks", "15", False),
    ("6.3. Real-Time Advanced Analytics", "15", False),
    ("6.4. IoT Device Monitoring Expansion", "15", False),
    ("6.5. Cloud & Edge Computing Integration", "15", False),
    ("6.6. Enhanced Security Features", "16", False),
    ("6.7. Automation & Self-Optimization", "16", False),
    ("6.8. User Experience Enhancements", "16", False),
    ("Conclusion", "17", False),
    ("Online Shopping System Testing Document", "17", False),
    ("7.1. Introduction", "17", False),
    ("7.1.1 Purpose", "17", False),
    ("7.1.2 Scope", "17", False),
    ("7.1.3 Objectives", "17", False),
    ("7.2. Test Plan", "18", False),
    ("7.2.1 Test Strategy", "18", False),
    ("The testing approach includes:", "18", False),
    ("7.2.2 Test Environment", "18", False),
    ("7.2.3 Test Schedule", "18", False),
    ("Defines timeline for:", "18", False),
    ("7.3 Functional Testing", "18", False),
    ("7.3.1 Test Cases", "18", False),
    ("7.3.2 Test Scenarios", "19", False),
    ("7.3.3 Test Data", "19", False),
    ("7.3.4 Test Execution", "19", False),
    ("7.4. Performance Testing", "19", False),
    ("7.4.1 Load Testing", "19", False),
    ("7.4.2 Stress Testing", "19", False),
    ("7.4.3 Performance Metrics", "19", False),
    ("7.5. Security Testing", "20", False),
    ("7.5.1 Authentication and Authorization", "20", False),
    ("7.5.2 Data Encryption", "20", False),
    ("7.5.3 Access Control", "20", False),
    ("7.6. Usability Testing", "20", False),
    ("7.6.1 User Interface", "20", False),
    ("7.6.2 Workflow Testing", "20", False),
    ("7.6.3 Accessibility", "20", False),
    ("7.7. Defect Management", "20", False),
    ("7.7.1 Defect Reporting", "20", False),
    ("7.7.2 Regression Testing", "20", False),
    ("7.8. Conclusion", "20", False),
]

for entry, page, bold in toc_data:
    dots = "." * max(2, 80 - len(entry) - len(page))
    fn = 'Times-Bold' if bold else 'Times-Roman'
    line = f'<font name="{fn}">{entry} {dots} {page}</font>'
    story.append(Paragraph(line, toc_entry))

story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — TOC continued
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("7.9. References ........................................................................21", toc_entry))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 blank (matches original page 4)
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("7.9. References", h2))
story.append(Spacer(1, 0.1*inch))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — Introduction
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Introduction", h1))
story.append(Paragraph(
    "The Software Requirements Specification (SRS) document provides a detailed "
    "description of the Online Shopping System. This system is designed to facilitate, "
    "manage, and streamline online retail operations in real time. It includes features "
    "such as product browsing, order management, payment processing, and reporting. The "
    "document serves as a guideline for developers, testers, and stakeholders to "
    "understand system functionality and constraints.", body))

story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("1.1 Purpose:", h2))
story.append(Paragraph("The purpose of this document is to clearly define the requirements of the Online "
    "Shopping System. It helps:", body))
story.append(bul("Developers understand system functionalities and implementation needs"))
story.append(bul("Stakeholders review system objectives and expected outcomes"))
story.append(bul("Testers verify system performance against requirements"))
story.append(bul("Administrators manage and monitor shopping operations efficiently"))

story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("1.2 Product Scope:", h2))
story.append(Paragraph("The Online Shopping System is designed to manage and streamline e-commerce "
    "operations efficiently. The key features include:", body))
story.append(bul("Real-time monitoring of orders, inventory, and sales performance"))
story.append(bul("Detection and alerting of payment failures and stock shortages"))
story.append(bul("Visualization of sales statistics through dashboards"))
story.append(bul("Data logging and report generation for analysis"))
story.append(bul("Secure user authentication and role-based access"))
story.append(Paragraph("The system aims to improve customer experience, reduce cart abandonment, and ensure "
    "optimal performance of online shopping services.", body))

story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("1.3 Definitions, Acronyms, and Abbreviations", h2))
story.append(bul("OSS: Online Shopping System"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6
# ══════════════════════════════════════════════════════════════════════════════
story.append(bul("SRS: Software Requirements Specification"))
story.append(bul("UI: User Interface"))
story.append(bul("KPI: Key Performance Indicator"))
story.append(bul("QoS: Quality of Service"))
story.append(bul("API: Application Programming Interface"))
story.append(bul("Admin: System administrator with full access"))
story.append(bul("User: Authorized person who accesses the shopping platform"))

story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("1.4 Technologies to be used", h2))
story.append(Paragraph("The following technologies will be used for developing the Online Shopping System:", body))
story.append(bul("Frontend: HTML, CSS, JavaScript (React.js optional)"))
story.append(bul("Backend: Python (Django/Flask) or Node.js"))
story.append(bul("Database: MySQL / PostgreSQL / MongoDB"))
story.append(bul("Data Processing & Analytics: Python libraries (Pandas, NumPy)"))
story.append(bul("Monitoring Tools: Prometheus, Grafana (for visualization)"))
story.append(bul("APIs: REST APIs for communication"))
story.append(bul("Deployment Tools: Docker, Kubernetes (optional)"))
story.append(bul("Operating System: Linux / Windows"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 7 — Overall Description
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Overall Description", h1))
story.append(Paragraph(
    "The Online Shopping System is designed to manage and streamline e-commerce "
    "operations in real time. It collects data from order and inventory components "
    "and displays key metrics such as sales volume, order status, and customer activity "
    "through a user-friendly dashboard. The system helps detect failures, generate alerts, "
    "and provide reports for better decision-making. It ensures efficient platform "
    "performance, reduced downtime, and secure access for users.", body))

story.append(Paragraph("2.1 Product Perspective", h2))
story.append(Paragraph(
    "The Online Shopping System is a standalone system that integrates with existing "
    "e-commerce infrastructure. It interacts with payment gateways, inventory systems, "
    "and external tools to collect and analyse performance data, providing a centralized "
    "platform for monitoring and management.", body))

story.append(Paragraph("2.2 User Characteristics and Classes", h2))
story.append(Paragraph(B("User Characteristics"), h3))
story.append(bul("Users include both technical (developers, admins) and non-technical (customers, managers)."))
story.append(bul("Varying experience levels: expert, intermediate, novice."))
story.append(bul("Users have role-based access (admin, seller, customer)."))
story.append(bul("Admins use the system continuously, while customers use it for browsing and purchasing."))

story.append(Paragraph(B("2.3 Classes of Users"), h2))
story.append(bul("System Administrator – Full control, system configuration and user management."))
story.append(bul("Seller/Vendor – Manages products, inventory, and order fulfillment."))
story.append(bul("Customer – Browses products, places orders, and tracks deliveries."))
story.append(bul("Manager/Analyst – Views reports and sales metrics."))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 8
# ══════════════════════════════════════════════════════════════════════════════
story.append(bul("Support Staff – Handles customer queries and order issues."))
story.append(bul("Security Analyst – Monitors security and prevents fraudulent transactions."))
story.append(Paragraph(
    "The Online Shopping System operates on cloud and on-premise servers with support for "
    "Linux and Windows operating systems. It requires a high-speed internet connection and "
    "is accessible through web-based interfaces (browsers). The system integrates with "
    "payment gateways, databases, and analytics tools, and supports real-time data "
    "processing and reporting.", body))

story.append(Paragraph("2.3.2 User Documentation", h3))
story.append(Paragraph(
    "The system provides user manuals, installation guides, and online help documentation "
    "to assist users in operating and managing the Online Shopping System. It includes "
    "step-by-step instructions, troubleshooting guides, and FAQs for different user roles.", body))

story.append(Paragraph("2.3.3 Software Interfaces", h3))
story.append(Paragraph(
    "The Online Shopping System interfaces with payment gateways, inventory management "
    "systems, and external logistics tools for order processing. It supports integration "
    "through APIs, protocols, and web services to ensure seamless communication between "
    "system components.", body))

story.append(Paragraph("2.3.4 Hardware Interfaces", h3))
story.append(Paragraph(
    "The system interacts with servers, barcode scanners, payment terminals, and "
    "networking devices for collecting and processing real-time transaction data.", body))

story.append(Paragraph("2.3.5 External Forces", h3))
story.append(Paragraph(
    "The system is affected by network traffic load, payment gateway availability, "
    "supply chain disruptions, and regulatory policies, which may impact performance.", body))

story.append(Paragraph("2.3.6 Dependencies", h3))
story.append(Paragraph(
    "The system depends on stable network connectivity, cloud services, payment APIs, "
    "and third-party logistics services for proper functioning.", body))

story.append(Paragraph("2.3.1. Operating Environment", h3))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 9
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("2.3.7 Constraints", h3))
story.append(Paragraph(
    "The system is constrained by hardware limitations, bandwidth availability, "
    "payment compliance (PCI-DSS), and adherence to e-commerce regulations.", body))

story.append(Paragraph("3.3 System Features", h2))
story.append(Paragraph("3.3.1 Functional Requirements", h3))
story.append(bul("Monitor real-time order processing (status, quantity, delivery time)."))
story.append(bul("Detect and report payment failures or inventory shortages."))
story.append(bul("Generate alerts and notifications for abnormal conditions."))
story.append(bul("Provide dashboards and reports for analysis."))
story.append(bul("Allow user management and role-based access control."))

story.append(Paragraph("3.3.2 Non-Functional Requirements", h3))
story.append(bul(B("Performance:") + " System should support real-time data processing."))
story.append(bul(B("Reliability:") + " Ensure high availability with minimal downtime."))
story.append(bul(B("Scalability:") + " Handle large-scale e-commerce transaction data."))
story.append(bul(B("Security:") + " Protect data with authentication and encryption."))
story.append(bul(B("Usability:") + " Provide a user-friendly interface."))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 10
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Commitment to delivering a high-quality university website", h2))
story.append(Paragraph(
    "The system is committed to delivering a reliable, secure, and user-friendly "
    "university website that ensures seamless access to information and services. "
    "It focuses on high performance, accessibility, data security, and regular "
    "updates to meet user needs and maintain quality standards.", body))

story.append(Paragraph("How testing contributes to user satisfaction and operational efficiency", h2))
story.append(Paragraph(
    "Testing ensures that the system is reliable, error-free, and performs as "
    "expected, leading to improved user satisfaction. It helps identify and fix "
    "issues early, ensuring a smooth and user-friendly experience. Additionally, "
    "testing enhances operational efficiency by reducing system failures, "
    "improving performance, and minimizing maintenance costs.", body))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 11 — Design Document
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph(B("ONLINE SHOPPING SYSTEM DESIGN DOCUMENT"), title_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("5.1 System Design (front-end design)", h2))
story.append(Paragraph("5.1.1 Use case diagram", h3))
story.append(Paragraph(
    "The use case diagram illustrates the interactions between system actors (Customer, "
    "Seller, Admin, Payment Gateway) and system functions such as browsing products, "
    "placing orders, managing inventory, processing payments, and generating reports.", body))
story.append(Spacer(1, 0.3*inch))

# Simple use case table placeholder
uc_data = [
    [Paragraph(B("Actor"), body), Paragraph(B("Use Cases"), body)],
    [Paragraph("Customer", body), Paragraph("Browse Products, Add to Cart, Place Order, Track Order, Make Payment", body)],
    [Paragraph("Seller/Admin", body), Paragraph("Manage Products, View Orders, Update Inventory, Generate Reports", body)],
    [Paragraph("Payment Gateway", body), Paragraph("Process Payment, Verify Transaction, Send Confirmation", body)],
    [Paragraph("System Admin", body), Paragraph("Manage Users, Configure System, Monitor Performance", body)],
]
uc_table = Table(uc_data, colWidths=[1.4*inch, 4.0*inch])
uc_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.8, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(uc_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("5.1.2 Class Diagram", h3))
story.append(Paragraph(
    "The class diagram defines the structure of the Online Shopping System, including "
    "classes such as User, Product, Order, Cart, Payment, and their relationships. "
    "Key classes include:", body))
story.append(bul(B("User") + " – ID, Username, Role, Email, Login(), Logout()"))
story.append(bul(B("Product") + " – ProductID, Name, Price, Stock, addProduct(), updateStock()"))
story.append(bul(B("Order") + " – OrderID, Status, Timestamp, placeOrder(), cancelOrder()"))
story.append(bul(B("Cart") + " – CartID, Items, addItem(), removeItem(), checkout()"))
story.append(bul(B("Payment") + " – PaymentID, Method, Status, processPayment(), refund()"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 12
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("5.1.3 Sequence Diagram", h3))
story.append(Paragraph(
    "The sequence diagram for the Online Shopping System shows the step-by-step "
    "interaction flow:", body))
seq_steps = [
    "1. Customer logs in through the Web UI",
    "2. UI sends authentication request to Backend Server",
    "3. Backend verifies credentials and returns Auth Success",
    "4. Dashboard is displayed to the Customer",
    "5. Customer browses products and adds items to cart",
    "6. UI requests product data from Backend",
    "7. Backend fetches product details from Database",
    "8. Customer proceeds to checkout and initiates payment",
    "9. Backend communicates with Payment Gateway",
    "10. Payment Gateway processes transaction and returns status",
    "11. Order is confirmed and stored in Database",
    "12. Confirmation notification sent to Customer",
    "13. Seller receives order notification",
    "14. Admin monitors order analytics on dashboard",
]
for step in seq_steps:
    story.append(Paragraph(step, bullet))

story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("5.1.4 Collaboration Diagram", h3))
story.append(Paragraph(
    "The collaboration diagram for the Online Shopping System illustrates the "
    "object interactions:", body))

collab = [
    B("Interaction Flow Summary:"),
    "1. Customer logs in through Web UI",
    "2-3. UI authenticates with Backend",
    "4. UI shows product dashboard",
    "5-6. UI requests product data from Backend",
    "7. Backend fetches data from Database",
    "8-9. Product data displayed to Customer",
    "10. Customer adds to cart and initiates checkout",
    "11. Backend processes order and payment",
    "12. Database stores order record",
    "13. UI shows order confirmation to Customer",
    "14-15. Customer sets delivery preferences",
    "16-17. Backend triggers fulfillment process",
    "18-19. Backend notifies UI; UI notifies Customer",
]
for item in collab:
    story.append(Paragraph(item, bullet))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 13 — DFD
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("5.1.5 Data Flow Diagram", h3))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph(B("Level 0 DFD"), h3))
story.append(Paragraph(
    "The Level 0 DFD shows the Online Shopping System as a single process receiving "
    "inputs from Customers (login, product search, orders), Sellers (product listings, "
    "inventory updates), and Payment Gateways (transaction confirmations). Outputs "
    "include order confirmations, invoices, dashboards, and notifications stored in "
    "the central Database.", body))

# Level 0 DFD table representation
l0_data = [
    [Paragraph(B("External Entity"), body), Paragraph(B("Input to System"), body), Paragraph(B("Output from System"), body)],
    [Paragraph("Customer / Admin", body), Paragraph("Login, Search, Orders, Payments", body), Paragraph("Dashboard, Confirmations, Alerts", body)],
    [Paragraph("Payment Gateway", body), Paragraph("Transaction Status", body), Paragraph("Payment Requests", body)],
    [Paragraph("Database", body), Paragraph("Stored Data", body), Paragraph("Store / Retrieve Data", body)],
]
l0_table = Table(l0_data, colWidths=[1.5*inch, 2.1*inch, 2.1*inch])
l0_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.8, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(l0_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph(B("Level 1 DFD"), h3))
story.append(Paragraph("The Level 1 DFD decomposes the system into four main processes:", body))
story.append(bul(B("1.1 Data Collection") + " – Receives raw data from product listings, customer actions, and payment systems → stores in Network Data Logs (D1)"))
story.append(bul(B("1.2 Data Processing & Analysis") + " – Processes collected data; aggregates order metrics and sales KPIs"))
story.append(bul(B("1.3 Alert Generation") + " – Produces alerts for failed payments, low stock, or unusual activity → stored in Alerts Database (D2)"))
story.append(bul(B("1.4 Report Management") + " – Generates sales and performance reports → stored in Reports Database (D3)"))
story.append(Paragraph("The User/Admin receives Alerts and Reports from D2 and D3 respectively.", body))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 14 — ER Diagram
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("5.2 Database Design", h2))
story.append(Paragraph("5.2.1 ER Diagram", h3))
story.append(Paragraph("The ER Diagram for the Online Shopping System includes the following entities and relationships:", body))

er_data = [
    [Paragraph(B("Entity"), body), Paragraph(B("Attributes"), body), Paragraph(B("Relationships"), body)],
    [Paragraph("USER/ADMIN", body), Paragraph("AdminID (PK), Name, Role, Email, AccessLevel", body), Paragraph("GENERATES Reports (1:N)", body)],
    [Paragraph("PRODUCT", body), Paragraph("ProductID (PK), Name, Category, Price, Stock, Status", body), Paragraph("BELONGS TO Order (N:M)", body)],
    [Paragraph("ORDER", body), Paragraph("OrderID (PK), CustomerID, Status, DateCreated, TotalAmount", body), Paragraph("PROCESSED FROM Cart (N:1)", body)],
    [Paragraph("CART", body), Paragraph("CartID (PK), CustomerID, Items, CreatedAt", body), Paragraph("GENERATES Order (1:N)", body)],
    [Paragraph("PAYMENT", body), Paragraph("PaymentID (PK), Method, Status, Timestamp, Amount", body), Paragraph("TRIGGERS Alert (1:N)", body)],
    [Paragraph("ALERT", body), Paragraph("AlertID (PK), Severity, Message, Timestamp, Status", body), Paragraph("SENDS TO Admin (N:1)", body)],
    [Paragraph("REPORT", body), Paragraph("ReportID (PK), Type, DateCreated, Content (Sales Metrics)", body), Paragraph("GENERATED BY Admin (N:1)", body)],
]
er_table = Table(er_data, colWidths=[1.2*inch, 2.3*inch, 2.0*inch])
er_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.8, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('FONTSIZE', (0,0), (-1,-1), 9),
]))
story.append(er_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 15 — Future Scope
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Future scope", h1))
story.append(Paragraph(
    "The Online Shopping System has strong potential for expansion and enhancement "
    "as technology evolves. The following points outline its future scope:", body))

story.append(Paragraph("6. 1. Integration with AI & Machine Learning", h3))
story.append(bul("Implement intelligent algorithms for " + B("predictive analysis") + " of customer behaviour"))
story.append(bul("Enable " + B("personalised recommendations") + " by automatically detecting user preferences"))
story.append(bul("Improve fraud detection using real-time learning models"))

story.append(Paragraph("6.2 Support for Advanced Payment Systems", h2))
story.append(bul("Integrate with cryptocurrency and " + B("next-generation payment technologies")))
story.append(bul("Handle higher transaction volumes, ultra-low latency, and advanced security protocols"))

story.append(Paragraph("6.3. Real-Time Advanced Analytics", h2))
story.append(bul("Incorporate " + B("big data analytics") + " for handling massive sales traffic"))
story.append(bul("Provide deeper insights through dashboards with real-time visualization"))

story.append(Paragraph("6.4. IoT Device Monitoring Expansion", ParagraphStyle('H2Bold',
    fontName='Times-Bold', fontSize=12, spaceAfter=4, spaceBefore=8, leading=16)))
story.append(bul("Extend monitoring to smart retail devices and " + B("IoT sensors")))
story.append(bul("Ensure efficient management of smart warehouses, healthcare retail, and industrial supply chains"))
story.append(bul("Ensure efficient management of smart cities, healthcare, and industrial IoT systems"))
story.append(bul("5. Cloud & Edge Computing Inte"))
story.append(bul("Use " + B("edge computing") + " for faster local data processing and reduced latency"))

story.append(Paragraph("6.5. Cloud & Edge Computing Integration", h2))
story.append(bul("Deploy system on " + B("cloud platforms") + " for scalability and flexibility"))
story.append(bul("Use " + B("edge computing") + " for faster local data processing and reduced latency"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 16
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("6.6. Enhanced Security Features", h2))
story.append(bul("Implement advanced cybersecurity mechanisms to prevent attacks"))
story.append(bul("Include intrusion detection and prevention systems (IDPS)"))
story.append(bul("Ensure secure data transmission and storage"))

story.append(Paragraph("6.7. Automation & Self-Optimization", h3))
story.append(bul("Enable automatic " + B("inventory optimization") + " based on sales patterns"))
story.append(bul("Reduce human intervention through automated decision-making systems"))
story.append(bul("Connect with " + B("order management systems (OMS)") + " and enterprise tools"))
story.append(bul("Enable seamless data exchange with third-party platforms"))

story.append(Paragraph("6.8. User Experience Enhancements", h2))
story.append(bul("Improve UI/UX with intuitive dashboards"))
story.append(bul("Provide customizable alerts, reports, and analytics views"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 17 — Conclusion + Testing Document
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph(B("Conclusion"), h1))
story.append(Paragraph(
    "The Software Requirements Specification (SRS) for the Online Shopping System "
    "defines the overall functionality, performance, and constraints of the system in a "
    "clear and structured manner. It outlines the key features such as real-time order "
    "monitoring, analysis, alert generation, and report management, ensuring efficient "
    "supervision of e-commerce operations.", body))
story.append(Paragraph(
    "This document serves as a foundation for developers, designers, and stakeholders to "
    "understand system requirements and expectations. By following this SRS, the system "
    "can be developed to be reliable, scalable, and secure, meeting the demands of modern "
    "high-speed digital commerce.", body))
story.append(Paragraph(
    "In conclusion, the Online Shopping System aims to enhance platform performance, "
    "reduce downtime, and provide accurate insights, making it an essential tool for "
    "managing next-generation e-commerce infrastructure.", body))

story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("Online Shopping System Testing Document", h1))
story.append(Paragraph("7.1. Introduction", h2))
story.append(Paragraph("7.1.1 Purpose", h3))
story.append(Paragraph("The purpose of this document is to outline the testing strategy and "
    "procedures for the Online Shopping System.", body))
story.append(Paragraph("7.1.2 Scope", h3))
story.append(Paragraph("This document covers functional, performance, security, and usability "
    "testing of the Online Shopping System.", body))
story.append(Paragraph("7.1.3 Objectives", h3))
story.append(bul("Ensure the reliability and correctness of the system"))
story.append(bul("Validate that the system meets specified requirements"))
story.append(bul("Identify and fix defects in the system"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 18
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("7.2. Test Plan", h2))
story.append(Paragraph("7.2.1 Test Strategy", h3))
story.append(Paragraph("The testing approach includes:", body))
story.append(bul("Functional Testing"))
story.append(bul("Performance Testing"))
story.append(bul("Security Testing"))
story.append(bul("Usability Testing"))
story.append(Paragraph("It also defines test levels, entry/exit criteria, and testing techniques.", body))

story.append(Paragraph("7.2.2 Test Environment", h3))
story.append(bul("Hardware: Servers, monitoring devices, user systems"))
story.append(bul("Software: OS (Windows/Linux), database, e-commerce tools"))
story.append(bul("Network: High-speed internet or simulated e-commerce environment"))

story.append(Paragraph("7.2.3 Test Schedule", h3))
story.append(Paragraph("Defines timeline for:", body))
story.append(bul("Test planning"))
story.append(bul("Test case design"))
story.append(bul("Test execution"))
story.append(bul("Defect fixing & retesting"))

story.append(Paragraph("7.3 Functional Testing", h2))
story.append(Paragraph("7.3.1 Test Cases", h3))
story.append(Paragraph("Test cases will cover:", body))
story.append(bul("Product browsing and search"))
story.append(bul("Data collection from orders/transactions"))
story.append(bul("Real-time order processing"))
story.append(bul("Alert generation for payment failures"))
story.append(bul("Report generation"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 19
# ══════════════════════════════════════════════════════════════════════════════
story.append(bul("User/Admin login & management"))

story.append(Paragraph("7.3.2 Test Scenarios", h3))
story.append(bul("Monitoring real-time order status"))
story.append(bul("Detecting payment failures"))
story.append(bul("Generating alerts on low stock threshold breach"))
story.append(bul("Viewing reports and analytics"))

story.append(Paragraph("7.3.3 Test Data", h3))
story.append(bul("Valid and invalid product/order inputs"))
story.append(bul("Simulated transaction data"))
story.append(bul("Fault/fraud simulation data"))

story.append(Paragraph("7.3.4 Test Execution", h3))
story.append(Paragraph("Includes:", body))
story.append(bul("Execution of test cases"))
story.append(bul("Defect reporting"))
story.append(bul("Retesting after fixes"))

story.append(Paragraph("7.4. Performance Testing", h2))
story.append(Paragraph("7.4.1 Load Testing", h3))
story.append(Paragraph("Test system performance under normal and peak traffic conditions.", body))

story.append(Paragraph("7.4.2 Stress Testing", h3))
story.append(Paragraph("Evaluate system behaviour under extreme transaction load and failures.", body))

story.append(Paragraph("7.4.3 Performance Metrics", h3))
story.append(bul("Response time"))
story.append(bul("Throughput"))
story.append(bul("Latency"))
story.append(bul("Resource utilization"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 20
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("7.5. Security Testing", h2))
story.append(Paragraph("7.5.1 Authentication and Authorization", h3))
story.append(Paragraph("Verify secure login and role-based access control.", body))
story.append(Paragraph("7.5.2 Data Encryption", h3))
story.append(Paragraph("Ensure secure transmission and storage of payment and customer data.", body))
story.append(Paragraph("7.5.3 Access Control", h3))
story.append(Paragraph("Prevent unauthorized access to sensitive shopping and transaction data.", body))

story.append(Paragraph("7.6. Usability Testing", h2))
story.append(Paragraph("7.6.1 User Interface", h3))
story.append(Paragraph("Evaluate ease of use, dashboard clarity, and navigation.", body))
story.append(Paragraph("7.6.2 Workflow Testing", h3))
story.append(Paragraph("Check efficiency of shopping workflows and order handling.", body))
story.append(Paragraph("7.6.3 Accessibility", h3))
story.append(Paragraph("Ensure system is usable for all users, including accessibility considerations.", body))

story.append(Paragraph("7.7. Defect Management", h2))
story.append(Paragraph("7.7.1 Defect Reporting", h3))
story.append(Paragraph("Track defects with severity and priority.", body))
story.append(Paragraph("7.7.2 Regression Testing", h3))
story.append(Paragraph("Ensure new updates do not introduce new issues.", body))

story.append(Paragraph("7.8. Conclusion", h3))
story.append(Paragraph(
    "This document summarizes the testing strategy for the Online Shopping System. "
    "It ensures that the system is reliable, secure, and performs efficiently under "
    "various conditions. The document should be updated as the system evolves and "
    "new features are introduced.", body))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 21 — References
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("7.9. References", h2))
story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("1. Software Engineering textbooks", body))
story.append(Paragraph("2. IEEE Testing Standards", body))
story.append(Paragraph("3. Online tools (SmartDraw, Visual Paradigm)", body))
story.append(Paragraph("4. Official documentation and resources", body))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print("Done:", OUTPUT)
