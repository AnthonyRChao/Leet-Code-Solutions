# https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        result = []
        local = []
        local_no_period = []
        local_split = []
        domain = []
        
        # split emails into local and domain lists
        for email in emails:
            local.append(email.split('@')[0])
            domain.append('@' + email.split('@')[1])
        
        # remove periods from local
        for value in local:
            if '.' in value:
                local_no_period.append(value.replace('.', ''))
            else:
                local_no_period.append(value)
                
        # split local by '+', keep index [0] 
        for value in local_no_period:
            if '+' in value:
                local_split.append(value.split('+')[0])
            else:
                local_split.append(value)
        
        # join local and domain
        for i, value in enumerate(local_split):
            result.append(value + domain[i])

        return len(set(result))
        
"""
Provided Solution

class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, _, domain = email.partition('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

... solution in Java

class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> seen = new HashSet();
        for (String email: emails) {
            int i = email.indexOf('@');
            String local = email.substring(0, i);
            String rest = email.substring(i);
            if (local.contains("+")) {
                local = local.substring(0, local.indexOf('+'));
            }
            local = local.replaceAll(".", "");
            seen.add(local + rest);
        }

        return seen.size();
    }
}

_Learnings | .partition() | .index() | listSlicing
"""
