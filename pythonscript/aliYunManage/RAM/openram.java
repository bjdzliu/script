package ram;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.SimpleTimeZone;
import java.util.UUID;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import org.apache.commons.codec.binary.Base64;


public class generatesing {
	private static final String ENCODING = "UTF-8";
	private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'";
	
	private static String percentEncode(String value) throws UnsupportedEncodingException {
        return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null;
    }
	
	private static String formatIso8601Date(Date date) {
        SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
        df.setTimeZone(new SimpleTimeZone(0, "GMT"));
        return df.format(date);
    }


	public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException {
		// TODO Auto-generated method stub
		
		final String HTTP_METHOD = "GET";

	    Map<String, String> parameters = new HashMap<String, String>();
	    // 加入请求参数
	    parameters.put("Action", "SubscriptionCreateOrderApi");
	    parameters.put("productCode", "ram");
	    parameters.put("ownerId", "1207511937833225");
	    parameters.put("Version", "2014-07-14");
	    parameters.put("AccessKeyId", "LTAI5OMxee3rRgax");
	    parameters.put("Timestamp", formatIso8601Date(new Date()));
	    parameters.put("SignatureMethod", "HMAC-SHA1");
	    parameters.put("SignatureVersion", "1.0");
	    parameters.put("SignatureNonce", UUID.randomUUID().toString());
	    parameters.put("Format", "json");

	    // 对参数进行排序
	    String[] sortedKeys = parameters.keySet().toArray(new String[]{});
	    Arrays.sort(sortedKeys);

	    final String SEPARATOR = "&";

	    // 生成stringToSign字符串
	    StringBuilder stringToSign = new StringBuilder();
	    stringToSign.append(HTTP_METHOD).append(SEPARATOR);
	    stringToSign.append(percentEncode("/")).append(SEPARATOR);

	    StringBuilder canonicalizedQueryString = new StringBuilder();
	    for(String key : sortedKeys) {
	        // 这里注意对key和value进行编码
	        canonicalizedQueryString.append("&")
	        .append(percentEncode(key)).append("=")
	        .append(percentEncode(parameters.get(key)));
	    }

	    // 这里注意对canonicalizedQueryString进行编码
	   stringToSign.append(percentEncode(
	        canonicalizedQueryString.toString().substring(1)));
	    
	   System.out.println(stringToSign.toString());
	   
	   
	
	    final String ALGORITHM = "HmacSHA1";
	    final String ENCODING = "UTF-8";
	    
	    // key is AccessKey Secret
	    String key = "a2Us3R2OuMnZ5KkWfc86MMd887992F&";

	    Mac mac = Mac.getInstance(ALGORITHM);
	    mac.init(new SecretKeySpec(key.getBytes(ENCODING), ALGORITHM));
	    byte[] signData = mac.doFinal(stringToSign.toString().getBytes(ENCODING));

	    String signature = new String(Base64.encodeBase64(signData));
	    System.out.println(signature);

	}


}
