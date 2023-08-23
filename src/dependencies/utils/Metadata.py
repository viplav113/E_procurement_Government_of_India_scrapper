class Metadata:
    def __init__(self):
        self.metadata = r'''
        Author: Viplav Patwardhan
        Date Of Creation: 13th February 2023
        Contents: Details of Various Tenders issued by Organizations under Government of India
        Data Source: https://etenders.gov.in/eprocure/app
        Method of Data Generation: Web-Crawling
        Tools Used: Python Selenium Library
        
        Fields:
            organisation_name
            number_of_tenders
            organisation_chain
            tender_reference_number
            tender_id
            withdrawal_allowed
            tender_type	form_of_contract
            general_technical_evaluation_allowed
            itemwise_technical_evaluation_allowed
            payment_mode
            is_multi_currency_allowed_for_boq
            is_multi_currency_allowed_for_fee
            allow_two_stage_bidding
            tender_category
            no._of_covers
            tender_fee_in_dollars
            fee_payable_to
            fee_payable_at
            tender_fee_exemption_allowed
            emd_amount_in_dollars
            emd_through_bg/st_or_emd_exemption_allowed
            emd_fee_type
            emd_percentage
            emd_payable_to
            emd_payable_at
            title
            work_description
            nda/pre_qualification
            independent_external_monitor/remarks
            tender_value_in_dollars	product_category
            sub_category
            contract_type
            bid_validity(days)
            period_of_work(days)
            location
            pincode
            pre_bid_meeting_place
            pre_bid_meeting_address
            pre_bid_meeting_date
            bid_opening_place
            should_allow_nda_tender
            allow_preferential_bidder
            published_date
            bid_opening_date
            document_download/sale_start_date
            document_download/sale_end_date
            clarification_start_date
            clarification_end_date
            bid_submission_start_date
            bid_submission_end_date
            name
            address
        '''
        
        
    def generate_meatdata(self):
        file = open('./metadata.txt','w',encoding='utf-8')
        file.writelines(self.metadata)
        file.close()
        