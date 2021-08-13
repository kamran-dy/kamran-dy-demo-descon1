# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import cx_Oracle

class HrLeave(models.Model):
    _inherit = 'hr.leave'
    
    
    
    def action_send_holiday_data(self):
        for leave in self:
            ACTIVITY_ID = 2
            OFFICE_EMP_ID = leave.employee_id.barcode.lstrip("0")
            APPROVED_BY = leave.employee_id.parent_id.barcode.lstrip("0")
            APPROVED_DATE = leave.approve_date if leave.approve_date else fields.date.today()
            COMPANY_ID = leave.employee_id.company_id.segment1
            CREATED_BY = leave.employee_id.barcode.lstrip("0")
            CREATION_DATE = leave.create_date
            EFFECTIVE_DATE = leave.request_date_from
            EMPLOYEE_ID = leave.employee_id.barcode.lstrip("0")
            END_DATE = leave.request_date_to
           
            FORWARDED_TO =  leave.employee_id.parent_id.barcode.lstrip("0")
            HR_ACTION_DATE =  False
            HR_APPROVAL_FLG = 0
            HR_APPROVAL_ID = 0
            HR_APPROVAL_REQUIRED = ' '
            LEAVE_DAYS = int(leave.number_of_days)
            LEAVE_DAY_TYPE = leave.leave_category  
            LEAVE_STATUS = 'A'
            LEAVE_TYPE_ID = 1
            REASON = leave.name
            REMARKS = 'Test'
            START_DATE = leave.request_date_from
            START_TIME = fields.date.today()
            TRANSACTION_ID = leave.id
            YEAR = 2021
            conn = cx_Oracle.connect('xx_odoo/xxodoo123$@//10.8.7.152:1523/test2')
            cur = conn.cursor()
            statement = 'insert into ODOO_LEAVE_TRANSACTION(ACTIVITY_ID,OFFICE_EMP_ID,APPROVED_BY, APPROVED_DATE, COMPANY_ID,CREATED_BY,CREATION_DATE,EFFECTIVE_DATE,EMPLOYEE_ID,END_DATE,  FORWARDED_TO, HR_APPROVAL_FLG, HR_APPROVAL_ID, HR_APPROVAL_REQUIRED, LEAVE_DAYS, LEAVE_DAY_TYPE, LEAVE_STATUS, LEAVE_TYPE_ID, REASON, REMARKS, START_DATE, TRANSACTION_ID,YEAR) values(: 2,:3,: 4,:5,: 6,:7,: 8,:9,: 10,:11,: 12,:13,: 14,:15,: 16,:17,: 18,:19,: 20,:21,: 22,:23,:24)'
            cur.execute(statement, (
            ACTIVITY_ID,OFFICE_EMP_ID,APPROVED_BY, APPROVED_DATE, COMPANY_ID,CREATED_BY,CREATION_DATE,EFFECTIVE_DATE,EMPLOYEE_ID,END_DATE,  FORWARDED_TO,  HR_APPROVAL_FLG, HR_APPROVAL_ID, HR_APPROVAL_REQUIRED, LEAVE_DAYS, LEAVE_DAY_TYPE, LEAVE_STATUS, LEAVE_TYPE_ID, REASON, REMARKS, START_DATE, TRANSACTION_ID,YEAR))
            conn.commit()
                        
            leave.action_send_holiday_line_data(leave.id)            
                        


    def action_send_holiday_line_data(self,leave):
        leaves = self.env['hr.leave'].search([('id','=',leave)]) 
        for leave in leaves:
            if leave.number_of_days >=  1:            
                for day in range(leave.number_of_days):            
                    EMPLOYEE_ID = leave.employee_id.barcode.lstrip("0")
                    ENABLED = 'Y'
                    LEAVE_DATE = leave.request_date_from
                    LEAVE_DAYS = -1
                    LEAVE_DAY_TYPE = leave.leave_category
                    if leave.leave_category == 'day':
                        LEAVE_DAY_TYPE = 'Full Day'  
                    if leave.leave_category == 'half_day':
                        LEAVE_DAY_TYPE = 'First Half'              
                    LTD_ID = leave.id 
                    TRANSACTION_ID = leave.id
                    YEAR = 2021            
                    conn = cx_Oracle.connect('xx_odoo/xxodoo123$@//10.8.7.152:1523/test2')
                    cur = conn.cursor()
                    statement = 'insert into ODOO_LEAVE_TRANSACTION_DTL(EMPLOYEE_ID,ENABLED, LEAVE_DATE, LEAVE_DAYS,LEAVE_DAY_TYPE,LTD_ID,TRANSACTION_ID,YEAR) values(: 2,:3,: 4,:5,: 6,:7,: 8,:9)'
                    cur.execute(statement, (
                    EMPLOYEE_ID,ENABLED, LEAVE_DATE, LEAVE_DAYS,LEAVE_DAY_TYPE,LTD_ID,TRANSACTION_ID,YEAR))
                    conn.commit()
        else:
             EMPLOYEE_ID = leave.employee_id.barcode.lstrip("0")
             ENABLED = 'Y'
             LEAVE_DATE = leave.request_date_from
             LEAVE_DAYS = -0.5
             LEAVE_DAY_TYPE = leave.leave_category
             if leave.leave_category == 'day':
                 LEAVE_DAY_TYPE = 'Full Day'  
             if leave.leave_category == 'half_day':
                 LEAVE_DAY_TYPE = 'First Half'              
             LTD_ID = leave.id 
             TRANSACTION_ID = leave.id
             YEAR = 2021            
             conn = cx_Oracle.connect('xx_odoo/xxodoo123$@//10.8.7.152:1523/test2')
             cur = conn.cursor()
             statement = 'insert into ODOO_LEAVE_TRANSACTION_DTL(EMPLOYEE_ID,ENABLED, LEAVE_DATE, LEAVE_DAYS,LEAVE_DAY_TYPE,LTD_ID,TRANSACTION_ID,YEAR) values(: 2,:3,: 4,:5,: 6,:7,: 8,:9)'
             cur.execute(statement, (
                EMPLOYEE_ID,ENABLED, LEAVE_DATE, LEAVE_DAYS,LEAVE_DAY_TYPE,LTD_ID,TRANSACTION_ID,YEAR))
             conn.commit()

